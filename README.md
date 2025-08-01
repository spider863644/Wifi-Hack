# Wifi-Hack

A cross-platform WiFi password brute-forcing tool that works on Windows, macOS, and Linux operating systems.

## 🌟 Features

- **Cross-Platform Support**: Works on Windows, macOS, and Linux
- **Automatic WiFi Interface Detection**: Dynamically detects correct WiFi interface on macOS
- **WiFi Network Discovery**: Displays available WiFi networks
- **Brute Force Attack**: Dictionary-based password cracking
- **Colored Terminal Output**: Enhanced user experience with colorama
- **Platform-Specific Commands**: Uses native networking tools for each OS
- **Smart Connection Logic**: Improved network connection detection and handling

## 🖥️ Platform Support

| Platform | Tools Used | Requirements |
|----------|------------|--------------|
| **Windows** | `netsh` | Built-in Windows utility |
| **macOS** | `networksetup`, `airport` | Built-in macOS utilities |
| **Linux** | `nmcli` (NetworkManager) | NetworkManager package |

## 📋 Prerequisites

### All Platforms
- **Python 3.6+**: Download from [python.org](https://www.python.org/downloads/)
- **Git**: Download from [git-scm.com](https://git-scm.com/downloads)

### Linux-Specific
```bash
# Ubuntu/Debian
sudo apt-get install network-manager

# CentOS/RHEL/Fedora
sudo yum install NetworkManager
# or
sudo dnf install NetworkManager
```

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/spider863644/WiFi-Hack
cd WiFi-Hack
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Tool
```bash
# Basic usage
python3 wifi.py

# For WiFi hacking on macOS/Linux (requires admin privileges)
sudo python3 wifi.py
```

## 📖 Usage

1. **Launch the tool**: 
   - Basic usage: `python3 wifi.py`
   - For WiFi hacking: `sudo python3 wifi.py` (macOS/Linux)
2. **Select an option**:
   - `[1]` Hack WiFi - Start brute force attack (requires admin privileges)
   - `[2]` Display available networks - Scan for WiFi networks
   - `[3]` Check version - Show tool version and platform info
   - `[4]` Report issues - Open GitHub issues page

3. **For WiFi hacking**:
   - Enter the target SSID (network name)
   - Provide path to your password wordlist file
   - The tool will attempt each password until successful

## 📁 File Structure

```
WiFi-Hack/
├── wifi.py              # Main script
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── config.xml          # Generated WiFi profile (Windows only)
```

## 🔧 Dependencies

- **colorama==0.4.6**: For colored terminal output

## ⚠️ Important Notes

### Security & Legal
- **Educational Use Only**: This tool is intended for educational purposes and authorized testing only
- **Permission Required**: Only use on networks you own or have explicit permission to test
- **Responsibility**: Users are responsible for complying with local laws and regulations

### Platform-Specific Behavior
- **Windows**: Creates XML profiles for WiFi connections
- **macOS**: 
  - Automatically detects WiFi interface (e.g., en0, en1, etc.)
  - Requires administrator privileges for network changes (`sudo`)
  - Uses `networksetup` and `airport` utilities
- **Linux**: Requires NetworkManager service to be running

## 🐛 Troubleshooting

### Common Issues

1. **Script stuck in loop or won't start (Fixed in v1.1+)**
   - Updated connection logic resolves infinite loop issues
   - Smart detection of WiFi vs mobile data connections

2. **"networksetup not found" (macOS)**
   - This utility should be built-in. Try running with `sudo`

3. **Wrong WiFi interface detected (Fixed in v1.1+)**
   - Script now automatically detects correct WiFi interface
   - No longer assumes en0 for all Mac systems

4. **"nmcli not found" (Linux)**
   - Install NetworkManager: `sudo apt-get install network-manager`

5. **Permission denied errors**
   - Run with administrator/root privileges when necessary
   - On macOS/Linux: `sudo python3 wifi.py`

6. **No networks showing**
   - Ensure WiFi adapter is enabled
   - Check if WiFi scanning requires elevated privileges

## 📞 Contact & Support

- **WhatsApp**: +2349052863644
- **Issues**: [GitHub Issues](https://github.com/spider863644/Wifi-Hack/issues)

## 📄 License

This project is for educational purposes only. Use responsibly and in accordance with local laws.

---

**Developer**: Spider Anongreyhat  
**Team**: TermuxHackz Society
