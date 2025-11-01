# Object-detectio-Security Surveillance System

A comprehensive home security surveillance application built with Python that uses computer vision and machine learning to detect intruders and send real-time alerts.

## Features

### Security & Detection
- **Real-time Person Detection**: Uses YOLOv5 model from Ultralytics to detect persons in camera feeds
- **Multi-Camera Support**: Monitor multiple camera sources simultaneously
- **Automatic Recording**: Records video clips when an intruder is detected
- **Email Alerts**: Sends instant email notifications when suspicious activity is detected
- **Cooldown System**: Configurable alert cooldown to prevent notification spam

### User Management
- Secure user registration and authentication
- Encrypted password storage using Fernet encryption
- Security questions for password recovery
- Forgot password and user ID recovery options

### Configuration Options
- Adjustable recording duration
- Multiple camera source configuration (webcam, IP cameras, video files)
- Custom video save directory
- Email notification settings
- Alert cooldown period customization

### User Interface
- Clean, modern Tkinter-based GUI
- Dark theme for comfortable viewing
- Live multi-camera feed display
- Easy-to-use control panel

## Requirements

### System Requirements
- Python 3.7 or higher
- Webcam or IP camera
- Windows/Linux/macOS

### Dependencies
```
opencv-python
ultralytics
cryptography
Pillow
numpy
tkinter (usually included with Python)
```

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/anbu-surveillance.git
cd anbu-surveillance
```

### 2. Install Dependencies
```bash
pip install opencv-python ultralytics cryptography Pillow numpy
```

### 3. Download YOLO Model
The application uses YOLOv5s model which will be automatically downloaded on first run. Ensure you have an internet connection during the first launch.

### 4. Gmail App Password Setup (for email alerts)
To send email alerts, you need to configure Gmail with an App Password:

1. Enable 2-Factor Authentication on your Google account
2. Go to Google Account Settings > Security > 2-Step Verification > App passwords
3. Generate a new app password for "Mail"
4. Use this password in the application settings (not your regular Gmail password)

## Configuration

### First-Time Setup
1. Run the application
2. Register a new user account
3. Log in with your credentials
4. Click "Settings" to configure:
   - Email credentials (sender email and app password)
   - Receiver email address
   - Camera sources (0 for default webcam, or IP camera URLs)
   - Recording duration in minutes
   - Video save directory
   - Security question and answer

### Camera Source Format
- **Webcam**: Use `0`, `1`, `2`, etc. for different connected cameras
- **IP Camera**: Use RTSP/HTTP URL (e.g., `rtsp://192.168.1.100:554/stream`)
- **Video File**: Use absolute file path for testing

### Multiple Cameras
Separate multiple camera sources with commas in the settings:
```
0,1,rtsp://192.168.1.100:554/stream
```

## Usage

### Starting Surveillance
1. Launch the application:
```bash
python anbu_surveillance.py
```
2. Log in with your credentials
3. Click "Start Surveillance" to begin monitoring
4. The system will automatically detect persons and trigger alerts/recordings

### Managing Alerts
- First detection triggers an email alert (if configured)
- Video recording starts automatically
- Cooldown period prevents excessive alerts
- All events are logged to `surveillance_app.log`

### Stopping Surveillance
Click the "Exit" button to safely stop all camera feeds and close the application.

## File Structure

```
anbu-surveillance/
├── anbu_surveillance.py    # Main application file
├── secret.key               # Encryption key (auto-generated)
├── config.json              # Application configuration
├── users.json               # User database (encrypted passwords)
├── surveillance_app.log     # Application logs
└── recordings/              # Saved video recordings
```

## Security Features

- **Password Encryption**: All passwords are encrypted using Fernet symmetric encryption
- **Secure Storage**: User credentials stored in encrypted JSON format
- **Security Questions**: Additional layer for password recovery
- **Session Management**: Secure login system with user authentication

## Troubleshooting

### Camera Not Opening
- Verify camera is connected and not used by another application
- Try different camera indices (0, 1, 2)
- Check camera permissions in your OS settings
- For IP cameras, verify RTSP/HTTP URL is correct

### Email Alerts Not Working
- Ensure you're using a Gmail App Password, not your regular password
- Check that sender email and password are correctly configured
- Verify receiver email address is valid
- Check internet connection

### YOLO Model Issues
- First run requires internet to download YOLOv5s model
- Model is cached locally after first download
- If issues persist, manually download from Ultralytics repository

### High CPU Usage
- Reduce number of camera feeds
- Lower recording quality in code (modify frame resolution)
- Increase sleep intervals in video loop

## Performance Tips

- Use lower resolution cameras for better performance
- Limit simultaneous camera feeds to 2-4 depending on system
- Ensure adequate storage space for video recordings
- Close other resource-intensive applications

## Future Enhancements

- [ ] Mobile web integration
- [ ] Cloud storage for recordings
- [ ] Advanced motion detection zones
- [ ] Email alert support
- [ ] Dashboard with analytics
- [ ] Multi-user access levels

## Known Limitations

- Email alerts require Gmail account with app password
- YOLO detection requires decent CPU/GPU for real-time processing
- Recording quality depends on camera specifications
- Storage requirements increase with longer recording durations

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**V Anbu Chelvan**
- GitHub: https://github.com/ZANYANBU)


## Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) for YOLOv5 implementation
- OpenCV community for computer vision tools
- Python community for excellent libraries

## Disclaimer

This software is intended for legitimate home security purposes only. Users are responsible for complying with local laws regarding surveillance and privacy. The author is not responsible for misuse of this software.

