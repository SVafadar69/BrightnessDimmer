$code = @"
using System;
using System.Runtime.InteropServices;
using System.Threading;

public class SleepHelper
{
    [DllImport("kernel32.dll", SetLastError = true)]
    public static extern uint SetThreadExecutionState(uint esFlags);

    [DllImport("user32.dll")]
    public static extern bool SendMessage(IntPtr hWnd, int Msg, int wParam, int lParam);

    public static void SleepSystem()
    {
        SetThreadExecutionState(0x80000002);
        SendMessage((IntPtr)0xffff, 0x0112, 0xf170, 2); // Turn off display
        Thread.Sleep(TimeSpan.FromMinutes(1));
        SetThreadExecutionState(0x80000000);
        SendMessage((IntPtr)0xffff, 0x0112, 0xf170, -1); // Turn on display
    }
}
"@

Add-Type -TypeDefinition $code

[SleepHelper]::SleepSystem()