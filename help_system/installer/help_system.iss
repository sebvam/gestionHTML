[Setup]
AppName=Sistema de Ayuda
AppVersion=1.0
DefaultDirName={pf}\Sistema de Ayuda
DefaultGroupName=Sistema de Ayuda
OutputBaseFilename=HelpSystemSetup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\app.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "config\*"; DestDir: "{app}\config"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "templates\*"; DestDir: "{app}\templates"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Sistema de Ayuda"; Filename: "{app}\app.exe"
Name: "{group}\Desinstalar Sistema de Ayuda"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\app.exe"; Description: "Ejecutar Sistema de Ayuda"; Flags: nowait postinstall skipifsilent
