# podman-manager
Python CLI tool for managing podman machine VM &amp; containers

<LeftMouse># 🐳 Podman Machine Manager

> A Python CLI tool for managing/automating lightweight Podman container runtime engines & containers with ease.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## ✨ Features

- 🚀 **Quick VM Control** - Start/stop your Podman machine with a single keystroke
- 📦 **Container Management** - Spin up or tear down your entire container stack via docker-compose
- 🎨 **Beautiful CLI** - Clean ASCII banner and intuitive menu interface
- ⚡ **Lightning Fast** - Minimal overhead, maximum efficiency

## 🎯 What It Does

Stop juggling terminal commands. This tool gives you a simple menu-driven interface to:

1. **Start/Stop Podman VM** - Control your Podman machine without remembering commands
2. **Manage Containers** - Use `podman-compose` to bring your entire stack up or down
3. **Monitor Status** - See your VM status at a glance

Perfect for developers running self-hosted services (Wiki.js, Vaultwarden, etc.) who want a quick way to manage everything.

## 🛠️ Prerequisites

- macOS with Podman installed
- Python 3.8+
- `podman-compose` installed (`brew install podman-compose`)
- A `docker-compose.yml` file with your container definitions

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/kurtoskolac/podman-manager.git
cd podman-manager

# Make it executable (optional)
chmod +x podman.py
```

## ⚙️ Configuration

Edit the `COMPOSE_PATH` variable in `podman.py` to point to your docker-compose file:

```python
COMPOSE_PATH = "~/Projects/self-hosted/docker-compose.yml"
```

## 🚀 Usage

```bash
python3 podman.py
```

You'll see a beautiful menu:

```
███████████████████████████████████████████████████████████████████
█                    PODMAN MACHINE MANAGER                        █
███████████████████████████████████████████████████████████████████

podman-machine-default: Currently running

1.) Start VM
2.) Stop VM
3.) Start Containers
4.) Stop Containers
5.) Refresh
0.) EXIT
```

Just type the number and hit enter. It's that simple.

## 🎮 Menu Options

| Option | Action |
|--------|--------|
| `1` | Start the Podman VM |
| `2` | Stop the Podman VM |
| `3` | Run `podman-compose up -d` (start all containers) |
| `4` | Run `podman-compose down` (stop all containers) |
| `5` | Refresh banner menu |
| `0` | Exit the program |

## 💡 Use Cases

- **Morning routine**: Start VM → Start containers → Get coffee ☕
- **End of day**: Stop containers → Stop VM → Close laptop
- **Quick testing**: Spin everything up, test, tear it down
- **Resource management**: Stop everything when you need CPU/RAM for other tasks

## 🏗️ How It Works

The script uses Python's `os.system()` to execute Podman commands:
- VM control via `podman machine start/stop`
- Container management via `podman-compose up/down`
- Status monitoring via `podman machine list`

## 🤝 Contributing

Got ideas? Found a bug? PRs welcome!

1. Fork it
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

## 📝 Roadmap

- [ ] Add container logs viewer
- [ ] Individual container control
- [ ] Resource usage monitoring
- [ ] Config file support (YAML/JSON)
- [ ] Color-coded status indicators

## 🐛 Known Issues

- Requires `podman-compose` to be in PATH
- Currently hardcoded compose path (config file coming soon)

## 📜 License

MIT License - do whatever you want with it!

## 👤 Author

**Danijel Taric**

- GitHub: [@kurtoskolac](https://github.com/kurtoskolac)

## 🙏 Acknowledgments

- Built for the self-hosting community
- Inspired by the need to manage Wiki.js, Vaultwarden, and other containers efficiently on Apple Silicon

Currently have a podman VM running 1 CPU & 640MB Memory w/ above containers, idle 150-200MB Memory used with over 450MB of overhead!
---

⭐ If this saved you some time, drop a star!
