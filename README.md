# TouchOSC Control Surface for Ableton Live

A custom control surface interface for **TouchOSC** designed to control **Ableton Live** for DJing. This layout provides track selection, track colors, and mixer controls using OSC and MIDI.

## 📂 Repository Structure

* **`ControlSurface.tosc`**: The layout file for the TouchOSC app.
* **`Live Template`**: Contains the Ableton Live project template for DJing.
    * `Template.als`: The Live Set file.

## 🛠 Prerequisites

Before using this control surface, ensure you have the following installed:

1.  **[TouchOSC](https://hexler.net/touchosc)** ($19.99) is installed on your tablet/phone and desktop editor.
2.  **Ableton Live**.
3.  **[AbletonOSC](https://github.com/ideoforms/AbletonOSC)**: This is required to handle the OSC communication.

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
![alt text](/img/1.png)
4.  Open the provided template file:
    * Go to `File` > `Open Live Set...`
    * Select `Live Template/Template.als` from this repository.

### 3. Configure TouchOSC
1.  Open **TouchOSC** on your device (iPad/Android/Desktop).
2.  Open the `.tosc` file:
    * Transfer `ControlSurface.tosc` to your device.
    * Open it in the TouchOSC editor/player.
3.  Set up the **OSC Connection** (On your tablet):
    * **Host (Send Port)**: IP address of your computer running Live (e.g., `192.168.x.x`). You can find it by typing `ipconfig` in the command prompt. 
    * **Port (Outgoing)**: `11000` (Default for AbletonOSC).
    * **Port (Incoming)**: `11001` (Default for AbletonOSC).
![alt text](/img/2.png)
4.  Set up the **MIDI Connection**:
    * Select your TouchOSC Bridge or MIDI interface. On Android, you can choose `MIDI option` directly in the notification bar when plug it in to your computer.
    * Add TouchOSC Bridge or MIDI interface to the **MIDI** section.<br>
![alt text](/img/3.png)<br>
![alt text](/img/4.png)

## 🎛 Features

* **Track Selection & Color Sync**:
    * Selecting a track in Live updates the grid on TouchOSC.
    * Pressing a track button on TouchOSC selects the track in Live.
    * Track headers on TouchOSC automatically match the track color in Ableton Live.

* **BPM changing**:
    * Change BPM on your surface control via OSC.
* **Mixer Controls**:
    * EQ adjustment & FX for 2 decks.
![alt text](/img/5.png)
![alt text](/img/6.png)

## 🔧 Troubleshooting

**The track selection works in Live but doesn't update on the iPad.**
* Ensure your firewall is not blocking UDP traffic on ports 11000/11001.
* Check that your computer and device are on the same Wi-Fi network.
