# UAV Telemetry Analysis

## 1. Classification: **Insufficient Evidence**

One feature, the jamming indicator, is rising. Nothing else in the data shows GNSS degradation. The window is too short, and the data looks too processed, to call this suspicious or benign with any confidence.

---

## 2. Supporting telemetry observations

I'm assuming the timestamps are in microseconds, which is the usual PX4 convention. Under that assumption the whole window lasts about **0.34 s** (375,399,167 → 375,735,466).

| Feature             | Start       | End         | Change                                   | What it shows                                                  |
| ------------------- | ----------- | ----------- | ---------------------------------------- | -------------------------------------------------------------- |
| `jamming_indicator` | 34.10       | 40.00       | +5.90 (+17%)                             | Rises every row by exactly the same step (0.6552)              |
| `satellites_used`   | 11          | 11          | none                                     | Constant                                                       |
| `fix_type`          | 3           | 3           | none                                     | 3D fix held the whole time                                     |
| `lat_x`             | 36.20482056 | 36.20482058 | about 2 mm                               | Effectively stationary                                         |
| `lon_x`             | 138.2529156 | 138.2529156 | none at the displayed precision (\~9 mm) | Effectively stationary                                         |
| `alt_x`             | 51.94241    | 51.95166    | +9.2 mm                                  | Tiny, smooth climb                                             |
| `vel_m_s`           | 0.0470      | 0.0330      | −0.014                                   | Near hover, falls every row by exactly the same step (0.00155) |

**Things about the data itself:**

- **The sampling is irregular.** Most gaps are 36–55 ms, but two are about 5 ms (rows 4→5 and 7→8).
- **Several columns look interpolated rather than measured.** The jamming indicator, velocity and altitude change by the same amount every row, whether the gap is 5 ms or 50 ms. Both the jamming and velocity steps work out to a span divided by 29. A real sensor wouldn't behave that way, so the data was probably resampled, or merged from different log topics. The `_x` column suffixes also suggest a merge.
- **Horizontal motion is a bit low for the reported speed.** 0.04 m/s over 0.34 s should move the drone roughly 11–16 mm, but only about 2 mm shows up. That gap is near the resolution of the displayed coordinates, so it's weak evidence at most.

---

## 3. Possible security-related explanations (hypotheses, not findings)

- **Early RF interference or low-power jamming.** A rising jamming indicator can come before any loss of satellites or fix. That fits "indicator up, everything else normal." But this window shows no actual degradation of positioning.
- **Spoofing.** Nothing here supports it: no position jump, no change in velocity, no change in satellite count. Telemetry this limited can't rule it out either.

---

## 4. Alternative non-malicious explanations

- **Interference from the drone itself.** ESCs, motors, video transmitters, companion computers or USB 3.0 devices near the GNSS antenna can raise the indicator.
- **Interference from nearby legitimate transmitters** in the area.
- **Normal variation.** The indicator's scale and normal baseline depend on the receiver, so 34–40 could be ordinary for this airframe. There's no baseline to compare against.
- **A preprocessing artifact.** The perfectly linear trends suggest interpolation. If so, the "rise" may just connect two real samples that were far apart, and it isn't evidence of a steady trend.
- **Normal noise.** The 9 mm altitude change and 2 mm horizontal drift are well within ordinary GNSS and barometer noise for a hovering drone.

---

## 5. Confidence: **Low**

My confidence that any attack is happening is low. I'm fairly confident that this data alone can't settle the question either way. The main limits are the 0.34 s window, the lack of a baseline, the missing GNSS quality fields, and signs that the data isn't raw.

---

## 6. Additional evidence needed to confirm an attack

1. **A longer window** before and after this one, plus a baseline jamming indicator from the same vehicle in known-clean conditions.
2. **Raw, uninterpolated logs** with the original timestamps for each topic.
3. **Receiver status fields:** `jamming_state`, `spoofing_state`, `noise_per_ms`, and AGC level if available.
4. **Accuracy metrics:** `eph`/`epv`, `hdop`/`vdop`, `s_variance_m_s`, `c_variance_rad`.
5. **Signal strength per satellite (C/N0).** A uniform drop across all satellites points to jamming. Unusually uniform or high values point to spoofing.
6. **Cross-sensor consistency:** EKF GPS innovations and test ratios, plus IMU, barometer and optical-flow agreement with the GNSS position and velocity.
7. **Correlation with onboard events:** throttle or motor changes, video transmitter power-up, payload activation.
8. **External corroboration:** an RF spectrum survey, a second GNSS receiver, or reports from other receivers in the area.

**Bottom line:** the rising jamming indicator is worth watching, but nothing else confirms it. Satellites, fix and position are all stable, and the linear pattern suggests interpolated data, so this window alone doesn't support calling the activity suspicious. [model opus 5.5]