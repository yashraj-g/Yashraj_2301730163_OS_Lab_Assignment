import subprocess
import uuid
def check_cpu_flags():
    """Check if 'hypervisor' flag is present in /proc/cpuinfo."""
    try:
        output = subprocess.check_output("cat /proc/cpuinfo", shell=True).decode()
        if "hypervisor" in output:
            return True
    except:
        pass
    return False
def check_dmi_data():
    """Check system manufacturer and product names for VM indicators."""
    indicators = ["VirtualBox", "VMware", "KVM", "QEMU", "Hyper-V", "Xen", "Bochs"]
    try:
        product = subprocess.check_output("cat /sys/class/dmi/id/product_name", shell=True).decode().strip()
        vendor = subprocess.check_output("cat /sys/class/dmi/id/sys_vendor", shell=True).decode().strip()
        for item in indicators:
            if item.lower() in product.lower() or item.lower() in vendor.lower():
                return True
    except:
        pass
    return False
def check_mac_address():
    """Check if MAC address belongs to known virtual NIC ranges."""
    vm_mac_prefixes = {
        "00:05:69", "00:0C:29", "00:1C:14", 
        "08:00:27",                          
        "52:54:00",                            
    }
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                   for ele in range(40, -1, -8)])
    mac_prefix = mac.upper()[0:8]
    return mac_prefix in vm_mac_prefixes
def is_virtual_machine():
    if check_cpu_flags():
        return True
    if check_dmi_data():
        return True
    if check_mac_address():
        return True
    return False
if __name__ == "__main__":
    if is_virtual_machine():
        print("⚠️ This system appears to be running inside a Virtual Machine.")
    else:
        print("✔️ This system appears to be running on Physical Hardware.")
