# kill-this-port

`kill-this-port` is a Python utility to quickly identify and kill processes running on a specified port. It is ideal for developers managing networked applications who often encounter port conflicts.

## Features
- **Check Port Usage**: View which processes are using a specific port.
- **Kill Processes**: Safely terminate processes occupying a port.
- **Force Kill**: Use a forceful approach to stop stubborn processes.

## Installation
Install the utility using pip:
```bash
pip install kill-this-port
```

## Usage
1. **Check Port Usage**:
   ```bash
   checkport [port]
   ```
   Example:
   ```bash
   checkport 8000
   ```

2. **Kill Process by Port**:
   ```bash
   killport [port]
   ```
   Example:
   ```bash
   killport 8000
   ```

3. **Force Kill Process by Port**:
   ```bash
   killport --force [port]
   ```
   Example:
   ```bash
   killport --f 8000
   ```

## Example
To check port `3000` usage:
```bash
checkport 3000
```

To kill the process using port `3000`:
```bash
killport 3000
```

To forcefully kill the process:
```bash
killport --force 3000
```

## Author
**Aaditya Kanjolia**

GitHub: [aadityakanjolia4](https://github.com/aadityakanjolia4)

