import speedtest
from rich.live import Live
from rich.table import Table
from datetime import datetime
import time

def test_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1e6
    upload_speed = st.upload() / 1e6
    ping = st.results.ping
    return round(download_speed, 2), round(upload_speed, 2), round(ping, 2)

def create_table(download, upload, ping):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    table = Table(title="Real-Time Internet Speed Monitor", style="bold cyan")
    table.add_column("Metric", justify="center", style="yellow", no_wrap=True)
    table.add_column("Value", justify="center", style="bold green")

    table.add_row("Current Time", current_time)
    table.add_row("Download Speed", f"{download} Mbps")
    table.add_row("Upload Speed", f"{upload} Mbps")
    table.add_row("Ping", f"{ping} ms")
    return table

if __name__ == "__main__":
    print("Testing Internet Speed... (Press CTRL+C to stop)\n")
    try:
        with Live(create_table(0, 0, 0), refresh_per_second=1) as live:
            while True:
                download_speed, upload_speed, ping = test_internet_speed()
                live.update(create_table(download_speed, upload_speed, ping))
                time.sleep(5)
    except KeyboardInterrupt:
        print("\nReal-Time Internet Speed Monitor Stopped.")
