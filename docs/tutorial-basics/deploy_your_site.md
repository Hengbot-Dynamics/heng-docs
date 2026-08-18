---
sidebar_position: 6
---

# Legacy Sirius v1.0 WebSocket API (Retired)

:::danger[This page is retired]

This chapter previously documented the WebSocket API of the **Sirius v1.0 firmware generation**. That
protocol and every command example it contained have been **retired and removed from this page**. Do
not use anything from the old version of this page against a robot.

:::

## 1. Status

- **Retired.** This page no longer contains an operating tutorial.
- The old endpoint form `ws://<IP>:10710/getjson` and its command vocabulary belong to the v1.0
  firmware generation only. They do **not** apply to current robots.
- Current robots expose a different local interface layer. Its behaviour is defined by the firmware
  actually installed on the robot, not by this page.

## 2. Why it was retired

- The old page shipped copy-and-paste commands that could unload motor torque, drive the robot at
  full speed, or change torque output limits. Published as-is, those are a physical hazard.
- It instructed readers to lower browser security settings in order to reach a plaintext WebSocket.
- It embedded real network details (addresses and network names) from a development environment.
- Its protocol no longer matches current robots, so following it produces either nothing or
  unpredictable behaviour.

## 3. Where to go instead

The current user documentation portal is:

[Hengbot Docs](https://user.hengbot.com/en/heng-docs/intro)

For interface work on a current robot, use the reference material that matches the firmware
installed on that specific robot, together with its runtime capability information. This page
deliberately does **not** reproduce an interface list, because a copied list drifts out of date the
moment the firmware changes.

## 4. Safety boundaries

If you do any development against a robot, treat these as hard rules:

- **Never lower your browser's security settings** to reach a plaintext WebSocket.
- **Never expose a robot's local ports to the public internet.** Local interfaces are meant for a
  trusted, controlled network only.
- **Never execute the historical samples** — torque-disable, torque-limit changes, full-speed motion
  and recording control included.
- Work in a cleared area, keep a person physically attending the robot, and use the official
  documentation and stopping procedure that match the target firmware.

## 5. A software stop is not an emergency stop

This applies to every generation of the product and is worth stating plainly:

- A stop request sent over a network interface is **software**. It travels through the link and
  through several processes; if any of them is down, blocked or disconnected, nothing stops.
- Different stop requests cover different things. Cancelling action playback (`ACTION_STOP_ALL`) is
  **not** the same as stopping the gait (`GAIT_STOP`) — the two are handled by different services,
  and neither is a physical emergency stop.
- Physical safety comes from a cleared area, an attending operator, and cutting power — never from a
  single message.

This page intentionally provides **no copy-and-paste motion commands** of any kind.

## 6. Where the old content went

The full historical content of this page is preserved in this repository's Git history. It is kept
for version archaeology only — to understand what the v1.0 generation looked like — and must not be
copied and executed.

## 7. About this page

The file name and URL are kept unchanged so that existing links and the sidebar position continue to
work. Only the content has been replaced.
