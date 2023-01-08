import subprocess

import hydra


@hydra.main(version_base="1.2", config_path="./config", config_name="docker.yaml")
def main(cfg):
    """Creates a Docker container based on config/docker.yaml"""
    subprocess.run(["docker", "create", "-i",
                    "-p", f"{cfg.jupyter_port_source}:{cfg.juypter_port_target}",
                    "-v", f"{cfg.secrets_volume_source}:{cfg.secrets_volume_target}",
                    "-v", f"{cfg.repo_volume_source}:{cfg.repo_volume_target}",
                    "--name", cfg.container_name,
                    "--env", f"USERNAME={cfg.USERNAME}",
                    cfg.image_name
                    ])


if __name__ == "__main__":
    main()
