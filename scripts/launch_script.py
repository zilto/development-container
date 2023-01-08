import subprocess

import hydra


@hydra.main(version_base="1.2", config_path="./config", config_name="launch_script.yaml")
def main(cfg):
    """Launch a Python script from within the Docker dev container"""

    # subprocess.run(["c:/program files/docker/docker/Docker Desktop.exe"])  # start docker

    # poll container status
    container_status = subprocess.run(["docker", "inspect", "--format", "'{{json .State.Running}}'", cfg.container_name],
                                      capture_output=True, encoding="utf8", check=True)

    # start container if needed
    if container_status.stdout == "'false'\n":
        subprocess.run(["docker", "start", cfg.container_name], check=True)

    # run script within container
    subprocess.run(
        [
            "docker", "exec", "-it", cfg.container_name, "//bin//bash", "-c",
            f"source /venv/bin/activate &&\
            cd /workspaces/{cfg.workspace} &&\
            python {cfg.python_script}.py"
        ], check=True
    )

    # subprocess.run(["docker", "stop", cfg.container_id])  # stop container


if __name__ == "__main__":
    main()
