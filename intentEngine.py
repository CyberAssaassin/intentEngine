import os
import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

def generate_config():
    # 1. Load site variables from YAML using your exact filename
    with open("siteVars.yaml", "r") as f:
        site_data = yaml.safe_load(f)

    # 2. Setup Jinja2 environment and load your exact template filename
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("routerTemplate.j2")

    # 3. Render the template by injecting variables
    rendered_config = template.render(site_data)

    print("=== Generated Device Configuration ===")
    print(rendered_config)

    # 4. Ensure the output directory exists for clean file management
    output_dir = "generated_configs"
    os.makedirs(output_dir, exist_ok=True)

    # 5. Save the rendered output inside the generated_configs folder
    output_filename = os.path.join(output_dir, f"{site_data['hostname']}_config.txt")
    with open(output_filename, "w") as f:
        f.write(rendered_config)
    
    print(f"\n[INFO] Configuration compiled and saved to '{output_filename}'")
    
    return rendered_config, site_data

def deploy_config(config_text, site_data):
    device = {
        "device_type": "cisco_ios",
        "ip": "127.0.0.1",
        "username": "admin",
        "password": "password",
        "port": 22,
        "fast_cli": True
    }

    print("\n[INFO] Connecting to device via Netmiko...")
    try:
        # Uncomment below when connected to a real sandbox/lab device
        # net_connect = Netmiko(**device)
        # output = net_connect.send_config_set(config_text.splitlines())
        # print(output)
        # net_connect.disconnect()
        print("[INFO] Netmiko integration ready. (Simulated push successful)")
    except Exception as e:
        print(f"[ERROR] Connection failed: {e}")

if __name__ == "__main__":
    config, data = generate_config()
    # deploy_config(config, data)

