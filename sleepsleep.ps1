$signature = @"
[DllImport("user32.dll", SetLastError = true)]
public static extern bool SystemParametersInfo(uint uiAction, uint uiParam, IntPtr pvParam, uint fWinIni);
"@

Add-Type -MemberDefinition $signature -Namespace ScreenSaver -Name Util

$SPI_SETSCREENSAVETIMEOUT = 0x001F
$SPIF_SENDCHANGE = 0x02

# Set the screensaver timeout to 30 seconds
[ScreenSaver.Util]::SystemParametersInfo($SPI_SETSCREENSAVETIMEOUT, 30, [IntPtr]::Zero, $SPIF_SENDCHANGE)

# Activate the screensaver
Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

namespace ScreenSaver
{
    public static class NativeMethods
    {
        [DllImport("user32.dll")]
        public static extern void SendMessage(IntPtr hWnd, uint Msg, IntPtr wParam, IntPtr lParam);
    }
}
"@

$HWND_BROADCAST = [IntPtr]0xffff
$WM_SYSCOMMAND = 0x0112
$SC_MONITORPOWER = 0xF170
$POWER_OFF = 0x0002

[ScreenSaver.NativeMethods]::SendMessage($HWND_BROADCAST, $WM_SYSCOMMAND, [IntPtr]$SC_MONITORPOWER, [IntPtr]$POWER_OFF)

# Wait for 30 seconds
Start-Sleep -Seconds 30

# Restore the original screensaver timeout
[ScreenSaver.Util]::SystemParametersInfo($SPI_SETSCREENSAVETIMEOUT, 0, [IntPtr]::Zero, $SPIF_SENDCHANGE)
