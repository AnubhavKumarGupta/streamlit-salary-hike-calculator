; Salary Hike Calculator - Inno Setup Script
; This creates a professional installer for Windows

[Setup]
; Basic Information
AppName=Salary Hike Calculator
AppVersion=1.0.0
AppPublisher=Your Name
AppPublisherURL=https://yourwebsite.com
AppSupportURL=https://yourwebsite.com
AppUpdatesURL=https://yourwebsite.com

; Installation Directory
DefaultDirName={autopf}\Salary Hike Calculator
DefaultGroupName=Salary Hike Calculator
DisableProgramGroupPage=yes

; Output
OutputDir=installer_output
OutputBaseFilename=SalaryHikeCalculator_Setup
SetupIconFile=app_icon.ico

; Compression
Compression=lzma
SolidCompression=yes

; Windows Version
WinVersionTooOldError=This application requires Windows 7 or later.
MinVersion=6.1

; Privileges
PrivilegesRequired=admin

; UI
WizardStyle=modern
; Uncomment and set path if you have custom images
; WizardImageFile=installer_image.bmp
; WizardSmallImageFile=installer_icon.bmp

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; The main executable (created from PyInstaller)
Source: "dist\launcher.exe"; DestDir: "{app}"; Flags: ignoreversion
; If you have additional files, add them here
; Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Start Menu shortcut
Name: "{group}\Salary Hike Calculator"; Filename: "{app}\launcher.exe"
Name: "{group}\{cm:UninstallProgram,Salary Hike Calculator}"; Filename: "{uninstallexe}"
; Desktop shortcut (if user selected it)
Name: "{autodesktop}\Salary Hike Calculator"; Filename: "{app}\launcher.exe"; Tasks: desktopicon

[Run]
; Option to launch app after installation
Filename: "{app}\launcher.exe"; Description: "{cm:LaunchProgram,Salary Hike Calculator}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
; Clean up on uninstall
Type: filesandordirs; Name: "{app}"

[Code]
// Custom code can go here if needed
