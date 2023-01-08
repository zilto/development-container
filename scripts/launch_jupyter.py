import subprocess

import hydra


@hydra.main(version_base="1.2", config_path="./config", config_name="launch_jupyter.yaml")
def main(cfg):
    """Launch Jupyter server from the Docker dev container; accessible from outside"""

    # poll container status
    container_status = subprocess.run(
        ["docker", "inspect", "--format", "'{{json .State.Running}}'", cfg.container_name],
        capture_output=True, encoding="utf8", check=True)

    # start container if needed
    if container_status.stdout == "'false'\n":
        subprocess.run(["docker", "start", cfg.container_name], check=True)

    # run Flow within container
    subprocess.run(
        [
            "docker", "exec", "-it", cfg.container_name, "//bin//bash", "-c",
            f"source /venv/bin/activate &&\
            cd /workspaces/{cfg.workspace} &&\
            jupyter notebook --ip 0.0.0.0 --no-browser --allow-root"
        ], check=True
    )


if __name__ == "__main__":
    main()
