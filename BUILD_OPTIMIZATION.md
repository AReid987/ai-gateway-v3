# AI Gateway Build Optimization

This document describes the resource optimizations needed for successful compilation of the AI Gateway project on macOS.

## Issue
The AI Gateway compilation fails with "Resource temporarily unavailable (os error 35)" errors when building native dependencies like `aws-lc-sys` and `jemalloc-sys`. This occurs due to insufficient system resource limits for the intensive parallel compilation process.

## Solution

### 1. Increase System Resource Limits

```bash
# Increase kernel-wide limits (requires sudo)
sudo sysctl -w kern.maxfiles=1048576
sudo sysctl -w kern.maxfilesperproc=65536

# Increase shell file descriptor limit
ulimit -n 65536
```

### 2. Reduce Build Parallelism

```bash
# Serialize Rust compilation
export CARGO_BUILD_JOBS=1

# Serialize native dependency builds  
export MAKEFLAGS=-j1
```

### 3. Temporarily Relax Release Profile

In `Cargo.toml`, modify the release profile:

```toml
[profile.release]
opt-level = 3
lto = false        # was: true
codegen-units = 8  # was: 1
strip = true
```

### 4. Clean Build

```bash
cargo clean
cargo build --release -j1
```

## Making Changes Permanent

### Session-Only (Recommended for Development)
The `sysctl` and `ulimit` changes above are temporary and will reset on logout/reboot.

### Persistent Changes (Optional)
To make changes permanent:

1. **File Descriptor Limits**: Add to `~/.zshrc` or `~/.bash_profile`:
   ```bash
   ulimit -n 65536
   ```

2. **Kernel Limits**: Create `/etc/sysctl.conf` (requires admin privileges):
   ```
   kern.maxfiles=1048576
   kern.maxfilesperproc=65536
   ```

3. **LaunchD Limits**: Add to `/etc/launchd.conf`:
   ```
   limit maxfiles 65536 1048576
   ```

## Verification

Check current limits:
```bash
sysctl -n kern.maxfiles kern.maxfilesperproc
ulimit -n
```

## CI/Production Notes

For CI environments or production builds, consider:
- Pre-configuring these limits in the build environment
- Using containerized builds with appropriate resource limits
- Documenting these requirements in deployment guides

## Restoring Original Settings

After successful build, you can restore the original release profile settings in `Cargo.toml` if desired:
```toml
[profile.release]
opt-level = 3
lto = true
codegen-units = 1
strip = true
```

## Troubleshooting

- If issues persist, try further reducing `CARGO_BUILD_JOBS` to 1
- Monitor system resources during build with `Activity Monitor` or `top`
- Check for competing processes that might be consuming resources