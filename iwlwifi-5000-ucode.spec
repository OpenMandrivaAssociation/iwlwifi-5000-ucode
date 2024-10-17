Summary:	Intel PRO/Wireless 5000AGN microcode
Name:		iwlwifi-5000-ucode
Version:	8.83.5.1
Release:	3
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-5000-ucode-%{version}.tgz
Source1:	http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-5000-ucode-8.24.2.12.tgz
Source2:	http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-5000-ucode-5.4.A.11.tar.gz
License:	Proprietary
Group:		System/Kernel and hardware
Url:		https://intellinuxwireless.org/
BuildArch:	noarch

%description
The file iwlwifi-5000-*.ucode provided in this package is required to be
present on your system in order for the Intel PRO/Wireless 5000AGN Network
Connection Adapter driver for Linux (iwlagn) to be able to operate on
your system.

%prep
%setup -q -a 1 -a 2

# provide old firmware with ucode_api=1 for compatibility with older kernels
cp iwlwifi-5000-ucode-5.4.A.11/iwlwifi-5000-1.ucode .
cp iwlwifi-5000-ucode-5.4.A.11/README.iwlwifi-5000-ucode \
   README.iwlwifi-5000-ucode-1
# provide old firmware with ucode_api=2 for compatibility with older kernels
cp iwlwifi-5000-ucode-8.24.2.12/iwlwifi-5000-2.ucode .
cp iwlwifi-5000-ucode-8.24.2.12/README.iwlwifi-5000-ucode \
   README.iwlwifi-5000-ucode-2
mv README.iwlwifi-5000-ucode README.iwlwifi-5000-ucode-5

%build

%install
install -d %{buildroot}/lib/firmware
install -m644 *.ucode %{buildroot}/lib/firmware/

%files
%doc LICENSE.* README.*
/lib/firmware/*.ucode
