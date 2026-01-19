import re
import os

# Boot log will be created in the same directory as this script
BOOT_LOG_PATH = os.path.join(os.getcwd(), "boot.log")


def create_sample_boot_log():
    """
    Creates a sample infotainment boot log file
    """
    sample_log = """
[ 1.200] systemd: Started Display Service.
[ 2.800] systemd: Started Audio Service.
[ 5.600] systemd: Started Bluetooth Service.
[ 9.450] systemd: Started Network Manager.
[ 15.900] systemd: Started Media Indexing Service.
[ 18.300] systemd: Started Navigation Engine.
"""
    with open(BOOT_LOG_PATH, "w") as file:
        file.write(sample_log.strip())


def parse_boot_log(file_path):
    """
    Parses boot log and extracts service startup times
    """
    services = {}

    with open(file_path, "r") as file:
        for line in file:
            match = re.search(
                r"\[\s*(\d+\.\d+)\]\s+systemd:\s+Started\s+(.+)\.",
                line
            )
            if match:
                time_stamp = float(match.group(1))
                service_name = match.group(2)
                services[service_name] = time_stamp

    return services


def suggest_optimization(service_name):
    """
    Returns optimization recommendation for a service
    """
    recommendations = {
        "Media Indexing Service": "Delay startup or use incremental indexing.",
        "Navigation Engine": "Load maps after UI initialization.",
        "Network Manager": "Initialize asynchronously to avoid UI blocking.",
        "Bluetooth Service": "Start scanning only after user interaction."
    }

    return recommendations.get(
        service_name,
        "Optimize dependencies and service startup order."
    )


def get_slow_services(services, count=3):
    """
    Returns top N slowest services
    """
    return sorted(
        services.items(),
        key=lambda item: item[1],
        reverse=True
    )[:count]


def main():
    if not os.path.exists(BOOT_LOG_PATH):
        create_sample_boot_log()

    services = parse_boot_log(BOOT_LOG_PATH)
    slow_services = get_slow_services(services)

    print("\n" + "-" * 55)
    print("   Infotainment Boot Time Optimization Report")
    print("-" * 55)

    for service, time in slow_services:
        print(f"\nService Name   : {service}")
        print(f"Startup Time  : {time} seconds")
        print(f"Recommendation: {suggest_optimization(service)}")

    print("\nAnalysis Completed Successfully ✔\n")


if __name__ == "__main__":
    main()
