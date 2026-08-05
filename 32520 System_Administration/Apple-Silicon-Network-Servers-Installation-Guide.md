# Apple Silicon Installation Guide

**Subject systems:** CentOS Stream 10 and Windows Server 2025  
**Cloud environments:** Not used

## Option 1 — Remote or On-Campus x86-64 PC (Recommended)

This is the complete environment and supports the supplied x86 OVAs.

1. Connect to the approved x86-64 Windows PC using the institution's remote-access method, or use the PC on campus.
2. If VMware Workstation Pro is not installed and local installation is permitted, [download it from Broadcom](https://knowledge.broadcom.com/external/article/344595/unable-to-download-vmware-workstation-pr.html).
3. Run an Administrator Command Prompt from the installer directory:

   ```cmd
   VMware-workstation-full-<version>.exe /s /v"/qn EULAS_AGREED=1"
   ```

4. Open VMware Workstation Pro and select **File → Open**.
5. Import the Windows Server 2025 OVA, then the CentOS Stream 10 OVA.
6. Attach both VMs to the VMware network specified by the lab and start them.
7. Verify each guest:

   **Windows Server**

   ```cmd
   systeminfo | findstr /B /C:"OS Name" /C:"System Type"
   ```

   **CentOS**

   ```bash
   uname -m
   sudo dnf upgrade --refresh -y
   ```

Expected architecture: `x64-based PC` and `x86_64`.

References: [Workstation unattended installation](https://knowledge.broadcom.com/external/article/319650/performing-a-silent-installation-of-vmwa.html) · [Import OVF/OVA](https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/25H2/using-vmware-workstation-pro/creating-virtual-machines-in-workstation-user-guide/importing-and-exporting-virtual-machines-in-workstation-pro/import-an-open-virtualization-format-virtual-machine.html)

## Option 2 — UTM x86-64 Emulation on Apple Silicon

This can run both systems locally, but it is slower and should be used for assessment only when approved.

1. Install [Homebrew](https://brew.sh/) if required, then install UTM:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   brew install --cask utm
   ```

2. Download the official installation media:
   - [Windows Server 2025 x64 ISO](https://www.microsoft.com/en-us/evalcenter/download-windows-server-2025)
   - [CentOS Stream 10 x86_64 ISO](https://www.centos.org/download/)
3. In UTM, create the Windows VM: **+ → Emulate → Windows → x86_64**, select the Windows ISO, and use the lab's CPU, memory and disk requirements.
4. Create the CentOS VM: **+ → Emulate → Linux → x86_64**, select the CentOS ISO, and use the lab's resource requirements.
5. Configure both VMs with the same UTM network mode required by the lab, then complete both OS installers.
6. Do not enable **Force multicore** unless directed; UTM warns that forced x86 multicore emulation on ARM can be unstable.
7. Verify and update:

   **Windows Server**

   ```cmd
   systeminfo | findstr /B /C:"OS Name" /C:"System Type"
   ```

   **CentOS**

   ```bash
   uname -m
   sudo dnf upgrade --refresh -y
   ```

Use the ISOs for this option; VMware OVA configuration is not automatically reproduced by UTM.

References: [UTM installation](https://docs.getutm.app/installation/macos/) · [UTM Homebrew package](https://formulae.brew.sh/cask/utm) · [UTM architecture and emulation limits](https://docs.getutm.app/settings-qemu/system/)

## Option 3 — Native CentOS Stream 10 ARM64 on Apple Silicon

This is fast but provides **CentOS only**. It does not provide the required Windows Server 2025 system.

1. Install UTM if it is not already installed:

   ```bash
   brew install --cask utm
   ```

2. Download the [CentOS Stream 10 ARM64 (`aarch64`) ISO](https://www.centos.org/download/).
3. In UTM, select **+ → Virtualize → Linux** and choose the ARM64 ISO.
4. Apply the lab's CPU, memory, disk and network settings, then complete installation.
5. Update and verify:

   ```bash
   sudo dnf upgrade --refresh -y
   uname -m
   ```

Expected architecture: `aarch64`.

Windows Server 2025 requires the x64 instruction set, so it cannot be added as a native ARM64 VM. Use Option 1 or 2 when both servers are required.

References: [CentOS Stream 10 downloads](https://www.centos.org/download/) · [Windows Server hardware requirements](https://learn.microsoft.com/en-us/windows-server/get-started/hardware-requirements) · [UTM virtualization versus emulation](https://docs.getutm.app/settings-qemu/system/)

## Selection

1. **Option 1:** standard choice for labs and assessments.
2. **Option 2:** local fallback when emulation is approved.
3. **Option 3:** CentOS-only practice; not a complete subject environment.
