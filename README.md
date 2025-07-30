# 🎬 NiftyPool - Advanced Animated Telegram Auto-Forwarder

A **visually stunning** and **professionally animated** Python Telegram script using Telethon library for premium-grade automation and message forwarding with spectacular visual effects.

## ✨ Amazing Features

### 🎨 **Spectacular Visual Experience**
- **Animated ASCII Art Logo** with typewriter effects
- **Beautiful Loading Animations** with progress bars
- **Smooth Menu Transitions** with fade-in effects
- **Success Celebrations** with rotating emoji animations 🎉✨🎊⭐🎁
- **Error Alerts** with visual warnings ❌⚠️💥🚫
- **Real-time Status Indicators** 🟢🟡🟠🔴
- **Professional Startup Sequence** with step-by-step initialization

### 🚀 **Advanced Automation Features**
- **Multiple Account Support** with secure session management
- **Auto-Forwarding System** without "Forwarded from" tag
- **Smart Restart System** - `/restart` command auto-launches forwarder
- **Command-Based Control** via Telegram bot commands
- **Auto Group Management** with permission checking
- **Rate Limiting Compliance** and flood protection
- **Data Persistence** using JSON and SQLite
- **Web Control Panel** with real-time analytics and monitoring
- **Detailed Analytics** with performance metrics and error tracking

### 🛡️ **Enterprise-Grade Reliability**
- **Crash-Proof Operation** with comprehensive error handling
- **Detailed Logging System** with rotation and error tracking
- **Automatic Recovery** from connection failures
- **Safe Session Management** with encryption
- **Database Integrity** with proper schema design

## 📋 Requirements

- **Python 3.7+** (Tested on Python 3.11.9)
- **Telegram API credentials** (API ID and API Hash)
- **Active Telegram account(s)**
- **Windows/Linux/macOS** support

## 🔧 Quick Installation

### **Method 1: Automated Setup (Recommended)**
```bash
# 1. Download/Clone the project
git clone https://github.com/HarshDhaka69/NiftySender.git
cd NiftySender

# 2. Run automated setup
python setup.py

# 3. Launch NiftyPool
python NiftySender.py
```

## 🎬 **Getting Started Experience**

### **1. 🚀 Spectacular Startup**
When you run `python NiftySender.py`, enjoy:
- Animated NiftyPool logo with typewriter effect
- Professional loading sequence with progress indicators
- Beautiful welcome celebration with emoji animations

### **2. 🎨 Interactive Animated Menu**
Experience the stunning main menu with:
- Fade-in header effects
- Loading dots before each option
- Smooth slide-in menu items
- Color-coded options with emojis

### **3. 📱 First Time Setup**
1. **Get API Credentials:**
   - Visit: https://my.telegram.org/apps
   - Create new application
   - Copy your `API ID` and `API Hash`

2. **Add Your First Account:**
   - Select `1. 📱 Add Account`
   - Enter API credentials (one-time setup)
   - Add phone number with country code
   - Enter verification code from Telegram
   - Enter 2FA password if enabled

3. **Start the Magic:**
   - Select `4. 🚀 Start NiftyForwarder`
   - Watch the animated connection sequence
   - Enjoy real-time status updates

## 🤖 **Telegram Bot Commands**

Once NiftyForwarder is running, use these commands in **any Telegram chat**:

| Command | Usage | Description | Animation |
|---------|-------|-------------|-----------|
| `/set 5` | Reply to message | Forward message every 5 minutes | ✅ Success celebration |
| `/list` | Any chat | Show all forwarding configurations | 📋 Detailed list display |
| `/remove` | Current chat | Stop forwarding in this chat | 🗑️ Removal confirmation |
| `/logs` | Any chat | Get current log file via Telegram | 📄 File transfer animation |
| `/restart` | Any chat | **Auto-restart & launch forwarder** | 🔄 Smart restart sequence |

### **🔄 Smart Restart Feature**
- Type `/restart` in any Telegram chat
- Script automatically restarts **AND** launches forwarder
- No need to manually select menu options
- Seamless forwarding resumption

## 📁 **Project Structure**

```
NiftyPool/
├── 🎬 NiftySender.py              # Main animated application (47KB, 1128 lines)
├── ⚙️  setup.py             # Automated setup script
├── 📚 README.md             # This comprehensive guide
├── 📦 requirements.txt      # Python dependencies
├── 📂 data/                 # Configuration & database
│   ├── config.json          # Application settings
│   └── accounts.db          # Account database (SQLite)
├── 📊 logs/                 # Detailed application logs
│   └── niftypool_*.log      # Daily rotated log files
├── 🔐 sessions/             # Encrypted Telegram sessions
│   └── session_*.session    # Individual account sessions
└── 💾 backups/              # Automatic backups (future use)
```

## 🎯 **Advanced Usage**

### **🔧 Menu Options Explained**

#### **1. 📱 Add Account**
- **Animated Experience:** Progress bars for each step
- **Smart Detection:** Auto-detects existing API credentials
- **2FA Support:** Seamless two-factor authentication
- **Visual Feedback:** Success celebrations for completion

#### **2. 🗑️ Remove Account**
- **Safe Removal:** Animated confirmation process
- **Complete Cleanup:** Removes database entries + session files
- **Visual Progress:** Loading bars during removal process

#### **3. 📊 Show Details**
- **Animated Display:** Information appears progressively
- **Comprehensive Info:** Account status, forwarding rules, statistics
- **Real-time Status:** Live connection indicators
- **Beautiful Formatting:** Color-coded status displays

#### **4. 🚀 Start NiftyForwarder**
- **Epic Startup:** Multi-stage animated initialization
- **Connection Progress:** Real-time account connection status
- **Live Monitoring:** Rotating status indicators while running
- **Command Reference:** Animated command list display

## 🎨 **Visual Experience Examples**

### **Startup Animation**
```
🚀 Initializing NiftyPool...
⠋ Loading components...
✓ Components loaded successfully!
📁 Setting up directories... ✓
📊 Initializing database... ✓
⚙️  Loading configuration... ✓
🔧 Setting up logging... ✓
🎨 Preparing user interface... ✓
🎉 NiftyPool is ready to launch!
```

### **Menu Animation**
```
    _   ___ ______        ____              __
   / | / (_) __/ /___  __/ __ \____  ____  / /
  /  |/ / / /_/ __/ / / / /_/ / __ \/ __ \/ / 
 / /|  / / __/ /_/ /_/ / ____/ /_/ / /_/ / /  
/_/ |_/_/_/  \__/\__, /_/    \____/\____/_/   
                /____/                        

Contact @ItsHarshX For More Information
══════════════════════════════════════════════════════════

 MAIN MENU 

⠋ Loading option 1...
1. 📱 Add Account
⠙ Loading option 2...
2. 🗑️ Remove Account
⠹ Loading option 3...
3. 📊 Show Details
⠸ Loading option 4...
4. 🚀 Start NiftyForwarder
⠼ Loading option 5...
5. ❌ Exit

✨ Select your choice: 
```

### **Success Animation**
```
🎉 Account added successfully! ✨
🎊 Account added successfully! ⭐
🎁 Account added successfully! 🎉
```

## 🔐 **Security & Privacy**

### **🛡️ Security Features**
- **Session Encryption** - All Telegram sessions use Telethon's built-in encryption
- **API Credentials Protection** - Secure local storage with proper file permissions
- **Database Security** - SQLite with transaction safety and proper schema
- **Rate Limiting** - Automatic compliance with Telegram's API limits
- **Auto-Leave Protection** - Automatically leaves groups without send permissions

### **📊 Logging & Monitoring**
- **Comprehensive Logging** - All activities logged with timestamps
- **Error Tracking** - Detailed error logs for troubleshooting
- **Performance Monitoring** - Track forwarding success/failure rates
- **Daily Log Rotation** - Automatic log file management
- **Telegram Log Access** - Get logs via `/logs` command

## 🚦 **Best Practices**

### **🎯 Recommended Usage**
1. **Start Small** - Test with one account and few groups first
2. **Monitor Logs** - Regularly check logs for any issues via `/logs` command
3. **Respect Limits** - Don't set very short forwarding intervals (minimum 1 minute)
4. **Backup Data** - Keep backups of `data/config.json` and `data/accounts.db`
5. **Update Regularly** - Keep dependencies updated with `pip install -U -r requirements.txt`

### **⚡ Performance Tips**
- **Optimal Intervals:** Use 5+ minutes for busy groups, 1-2 minutes for quiet ones
- **Account Management:** Monitor account status regularly via menu option 3
- **Resource Usage:** The script is lightweight but monitor system resources with many accounts
- **Network Stability:** Ensure stable internet connection for best performance

## 🛠️ **Troubleshooting**

### **🔧 Common Issues & Solutions**

#### **1. 🔴 API Errors**
- **Issue:** "Invalid API ID/Hash"
- **Solution:** Verify credentials at https://my.telegram.org/apps
- **Check:** Ensure no extra spaces or characters in API credentials

#### **2. 📱 Session Issues**
- **Issue:** "Authentication failed"
- **Solution:** Delete session files and re-authenticate
- **Location:** Check `sessions/` directory for `.session` files

#### **3. 🚫 Permission Errors**
- **Issue:** "No permission to send messages"
- **Solution:** Ensure account has send permissions in target groups
- **Auto-Fix:** Script automatically leaves restricted groups if `auto_leave: true`

#### **4. ⏰ Rate Limiting**
- **Issue:** "FloodWaitError" in logs
- **Solution:** Script handles this automatically - no action needed
- **Prevention:** Use reasonable forwarding intervals (5+ minutes recommended)

#### **5. 🔄 Restart Issues**
- **Issue:** `/restart` command not working
- **Solution:** Ensure the bot account has proper permissions in the chat
- **Alternative:** Manually restart using `Ctrl+C` and `python main.py`

### **📋 Error Log Analysis**
Check `logs/niftypool_YYYYMMDD.log` for detailed error information:
- **INFO** - Normal operation messages
- **WARNING** - Non-critical issues (rate limits, permissions)
- **ERROR** - Serious issues requiring attention
- **DEBUG** - Detailed technical information

## 📞 **Support & Contact**

### **🆘 Getting Help**
- **Primary Contact:** @ItsHarshX (Telegram)
- **Log Analysis:** Use `/logs` command to get current log file
- **Error Reporting:** Include full error message and steps to reproduce
- **Feature Requests:** Contact via Telegram with detailed requirements

### **🤝 Contributing**
- **Bug Reports:** Provide detailed reproduction steps
- **Feature Ideas:** Suggest improvements via Telegram
- **Code Contributions:** Fork, improve, and create pull requests
- **Documentation:** Help improve this README

## ⚠️ **Important Legal Notes**

### **📜 Terms of Use**
- **Educational Purpose** - This project is for educational and personal use
- **Telegram ToS** - Ensure compliance with Telegram's Terms of Service
- **Rate Limits** - Respect Telegram's API rate limits (handled automatically)
- **Privacy** - Be mindful of message privacy and user permissions
- **Responsibility** - Use responsibly and ethically

### **🚫 Prohibited Uses**
- **No Spam** - Don't use for unsolicited bulk messaging
- **No Harassment** - Respect user privacy and consent
- **No Commercial Abuse** - Don't violate Telegram's commercial use policies
- **No Malicious Activity** - Use only for legitimate automation purposes

## 🎊 **Changelog & Updates**

### **🆕 Latest Version Features (Current)**
- ✅ **Spectacular Animations** - Full visual experience overhaul
- ✅ **Smart Restart System** - `/restart` auto-launches forwarder
- ✅ **Enhanced Error Handling** - Crash-proof operation
- ✅ **Improved UI/UX** - Professional visual feedback
- ✅ **Better Performance** - Optimized code and memory usage
- ✅ **Comprehensive Logging** - Detailed activity tracking

### **🔮 Coming Soon**
- 🔄 **Multi-language Support** - Interface in multiple languages  
- 📊 **Advanced Statistics** - Detailed forwarding analytics
- 🔒 **Enhanced Security** - Additional encryption options
- 🌐 **Web Interface** - Optional web-based control panel
- 📱 **Mobile App** - Companion mobile application

## 🎉 **Ready to Experience the Magic?**

```bash
# Quick Start (3 commands only!)
git clone https://github.com/HarshDhaka69/NiftySender.git && cd NiftySender
python setup.py
python main.py
```

**🎬 Welcome to the most beautiful Telegram forwarder ever created!**

**✨ Enjoy the spectacular visual experience and professional-grade automation!**

---

*Developed with ❤️ by @ItsHarshX | Contact for custom development and support* 
