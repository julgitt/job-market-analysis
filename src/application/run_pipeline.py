import subprocess
import sys


def run_step(command):
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command)
    if result.returncode != 0:
        print(f"Error executing: {' '.join(command)}")
        sys.exit(1)


if __name__ == "__main__":
    print("--- PIPELINE START ---")
    run_step([sys.executable, "-m", "src.application.fetch_job_offers"])
    run_step([sys.executable, "-m", "src.application.clean_job_offers"])
    run_step([sys.executable, "-m", "pytest"])
    run_step([sys.executable, "-m", "src.application.build_serving_data"])

    print("Pipeline finished successfully")