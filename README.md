# TouchOSC Control Surface for Ableton Live

A custom control surface interface for **TouchOSC** designed to control **Ableton Live** for DJing. This layout provides track selection, track colors, and mixer controls using OSC and MIDI.

## 📂 Repository Structure

* **`ControlSurface.tosc`**: The layout file for the TouchOSC app.
* **`Live Template/`**: Contains the Ableton Live project template optimized for DJing.
    * `Template.als`: The Live Set file.

## 🛠 Prerequisites

Before using this control surface, ensure you have the following installed:

1.  **[TouchOSC](https://hexler.net/touchosc)** (Mk2 / Next) installed on your tablet/phone and desktop editor.
2.  **Ableton Live** (Version 10/11/12).
3.  **[AbletonOSC](https://github.com/ideoforms/AbletonOSC)**: This is required to handle the OSC communication.
    * *Note: Ensure you are using a version of AbletonOSC that supports integer/float type handling or apply the fix detailed in the "Troubleshooting" section.*

## Installation & Setup

### 1. Install the Remote Script
1.  Download and install **AbletonOSC** into your Ableton Remote Scripts folder.
    * *Windows*: `\ProgramData\Ableton\Live x.x\Resources\MIDI Remote Scripts\`
    * *Mac*: `/Applications/Ableton Live x.x.app/Contents/App-Resources/MIDI Remote Scripts/`
2.  Restart Ableton Live.

### 2. Configure Ableton Live
1.  Open **Ableton Live**.
2.  Go to **Preferences** > **Link/Tempo/MIDI**.
3.  Add `AbletonOSC` as a Control Surface.
4.  Open the provided template file:
    * Go to `File` > `Open Live Set...`
    * Select `Live Template/Template.als` from this repository.

### 3. Configure TouchOSC
1.  Open **TouchOSC** on your device (iPad/Android/Desktop).
2.  Open the `.tosc` file:
    * Transfer `ControlSurface.tosc` to your device.
    * Open it in the TouchOSC editor/player.
3.  Set up the **OSC Connection**:
    * **Host (Send Port)**: IP address of your computer running Live (e.g., `192.168.1.5`).
    * **Port (Outgoing)**: `11000` (Default for AbletonOSC).
    * **Port (Incoming)**: `11001` (Default for AbletonOSC).
4.  Set up the **MIDI Connection**:
    * Select your TouchOSC Bridge or MIDI interface.

## 🎛 Features

* **Track Selection**:
    * Selecting a track in Live updates the grid on TouchOSC.
    * Pressing a track button on TouchOSC selects the track in Live.
* **Color Sync**:
    * Track headers on TouchOSC automatically match the track color in Ableton Live.
* **Mixer Controls**:
    * [List other controls here, e.g., Volume Faders, Pan, Sends].

## 🔧 Troubleshooting

**The track selection works in Live but doesn't update on the iPad.**
* Ensure your firewall is not blocking UDP traffic on ports 11000/11001.
* Check that your computer and device are on the same Wi-Fi network.
