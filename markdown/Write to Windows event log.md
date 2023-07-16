# Write to Windows event log

## Task Link
[Rosetta Code - Write to Windows event log](https://rosettacode.org/wiki/Write_to_Windows_event_log)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Locale;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

public class WriteToWindowsEventLog {
    public static void main(String[] args) throws IOException, InterruptedException {
        String osName = System.getProperty("os.name").toUpperCase(Locale.ENGLISH);
        if (!osName.startsWith("WINDOWS")) {
            System.err.println("Not windows");
            return;
        }

        Process process = Runtime.getRuntime().exec("EventCreate /t INFORMATION /id 123 /l APPLICATION /so Java /d \"Rosetta Code Example\"");
        process.waitFor(10, TimeUnit.SECONDS);
        int exitValue = process.exitValue();
        System.out.printf("Process exited with value %d\n", exitValue);
        if (exitValue != 0) {
            InputStream errorStream = process.getErrorStream();
            String result = new BufferedReader(new InputStreamReader(errorStream))
                .lines()
                .collect(Collectors.joining("\n"));
            System.err.println(result);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import win32api
import win32con
import win32evtlog
import win32security
import win32evtlogutil

ph = win32api.GetCurrentProcess()
th = win32security.OpenProcessToken(ph, win32con.TOKEN_READ)
my_sid = win32security.GetTokenInformation(th, win32security.TokenUser)[0]

applicationName = "My Application"
eventID = 1
category = 5	# Shell
myType = win32evtlog.EVENTLOG_WARNING_TYPE
descr = ["A warning", "An even more dire warning"]
data = "Application\0Data".encode("ascii")

win32evtlogutil.ReportEvent(applicationName, eventID, eventCategory=category, 
	eventType=myType, strings=descr, data=data, sid=my_sid)

```

