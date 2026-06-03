# AltitudeNow Privacy Policy

**Effective Date: May 27, 2026**

**Last Updated: June 3, 2026**

---

## Introduction

Welcome to AltitudeNow!

This Privacy Policy applies to the AltitudeNow app and related services you use (the "App"). We understand that your privacy matters. We are committed to handling your information in a transparent and restrained manner, and to keeping your data on your device whenever possible. This Privacy Policy is designed to help you understand:

- What information we collect
- How we use that information
- Your control over your information
- How we protect your information

Please read this Privacy Policy carefully. By downloading, installing, or using the App, you agree to the practices described in this policy.

---

## 1. Information We Collect

### 1.1 Information We Collect or Process

AltitudeNow processes data on a "local-first, minimum necessary" basis. We may collect or process the following information:

#### 1.1.1 Information You Provide or That Is Generated Through Use

- **Location and altitude information**: After you grant location permission, we read your device's GPS coordinates, altitude, vertical accuracy, heading (for the compass), and related data to display real-time altitude, resolve place names, generate summit/track cards, record track routes, and display the Summit Passport
- **Track route data**: When you use track recording, we continuously record GPS coordinate sequences, distance, duration, speed, and other activity metrics, and save route JSON files locally; **while track recording is in progress**, the App may continue to obtain location updates in the background (the exact mechanism depends on your device system, such as background location or a foreground service notification)
- **Photos and images**: When you use the summit camera or mark an arrival with a one-tap theme background Pin, the App captures or generates images; summit cards and track cards may include your photos plus overlaid text and graphics
- **Arrival record data**: Including capture or save time, altitude, latitude and longitude, place text, selected template, activity metrics (such as distance, elevation gain, and duration), and local image file paths
- **Track record data**: Including end time, start/end/route coordinates, distance, duration, average speed, end-point altitude, card image path, route file path, and template identifier
- **Summit Passport data**: Visit point information (coordinates, source type, etc.) aggregated on your device from local arrival and track records for map Pin display; this data is derived from on-device records and is not uploaded to our servers
- **App settings**: Such as altitude units (meters/feet), track distance units, language preference, haptic feedback toggle, map theme, summit theme colors, and other preferences stored on your device
- **Free quota counters**: To enforce free-tier limits (such as summit capture counts and track recording counts), the App stores related usage counters on your device

#### 1.1.2 Automatically Collected Information

- **Device and sensor information**: On supported devices, the barometer reads pressure and estimates oxygen-related data for on-screen display or card/weather ambience; the compass reads device orientation sensor data; the above data is processed locally and is not uploaded to our servers by default
- **Device information**: To keep the App running properly, we may obtain basic technical information through system interfaces such as device model, operating system version, app version, and language/region settings (for compatibility checks, version update detection, and bug fixes, and not to identify a specific natural person)
- **Version update detection information**: The App may send app identifier information to public app store query interfaces to obtain the latest version number and determine whether an update prompt is needed; this process does not involve your personal identity or business data
- **Subscription entitlement status**: When you purchase Pro membership, the app store verifies transactions and subscription status through its in-app purchase system; we only read verification results locally on your device to unlock features and **do not collect or store your payment card numbers or other financial information ourselves**

#### 1.1.3 Information Processed Over the Network (Not Stored on Our Servers by Default)

In the following scenarios, some data may leave your device, but **we do not use it to build user profiles on our own servers or to store your personal movement history long term**:

- **Reverse geocoding**: To convert coordinates into place names, latitude and longitude may be sent to geocoding services provided by the device system or third parties; this processing is governed by the relevant service provider's privacy policy
- **Weather queries**: Weather conditions may be obtained through third-party weather data services such as Apple WeatherKit or Open-Meteo; requests are initiated directly by your device, typically containing only approximate latitude and longitude and necessary query parameters, and we do not retain those requests on our servers; if WeatherKit is used, the App displays Apple Weather attribution
- **Map services**: Track maps, Summit Passport, and related features may use system maps or map SDKs such as Google Maps; during map loading your device may communicate with map service providers (such as map tile requests), which may involve approximate location information

### 1.2 Information We Do Not Collect

Except when you contact us directly, we **do not proactively collect** the following:

- Your name, national ID number, bank account details, or other strong identity identifiers
- Your contacts, SMS messages, or call logs
- Your Apple ID, Google account password, or other account credentials
- Advertising identifiers used for cross-app tracking (this App is not designed for ad tracking)
- Continuous background location when you are not using related features (the App may continue location updates in the background only **while track recording is in progress**; otherwise it primarily uses "While Using the App" location)
- Unified accounts or cloud business data backups (the current version requires no registration, and data is stored independently on your device by default)

---

## 2. How We Use Information

### 2.1 How We Use Your Information

Information we collect or process is used only for the following purposes:

#### 2.1.1 Providing Core Features

- **Real-time altitude and place display**: Using location and altitude data to show your current status on the summit screen
- **Compass**: Displaying bearing, latitude and longitude, and current altitude
- **Summit camera and card generation**: Combining photos or theme backgrounds with altitude, place, pressure, time, and other information into shareable cards
- **Track recording and track cards**: Recording routes, calculating distance/speed/duration, and generating shareable cards with route snapshots
- **Arrival records and track records**: Saving, displaying, and managing your historical records locally on your device
- **Summit Passport (Pro)**: Aggregating and displaying Pins for places you have visited on your device
- **Export and sharing**: Saving cards to the system photo library when authorized, or letting you choose recipients through the system share sheet
- **Settings and units**: Remembering your units, language, and related preferences
- **Pro membership benefits**: Unlocking corresponding features based on platform in-app purchase verification results

#### 2.1.2 Improving the App Experience

- **Performance optimization**: Analyzing necessary diagnostic and version information to improve stability
- **Feature improvement**: Understanding feature usage (if anonymous analytics services are integrated in the future, this policy will be updated accordingly)
- **Bug fixes**: Collecting necessary diagnostic information to resolve defects quickly
- **Version update prompts**: Comparing store version numbers and prompting you to update when appropriate

### 2.2 How We Will Not Use Your Information

We promise that we will **not**:

- Sell, rent, or trade your personal information to third parties
- Use your arrival records, tracks, or photos for unauthorized advertising
- Share personally identifiable information with other companies or organizations (except as required by law or with your explicit consent)
- Use your data for purposes not described in this policy without notice

---

## 3. Information Storage

### 3.1 Local Storage

AltitudeNow uses a **local-first** data storage strategy:

- **Arrival records, track records, and related metadata** are stored in the App's private database on your device
- **Summit/track card images** are saved in the app sandbox (such as Application Support / app-private storage) and/or in the system photo library if you choose to save them there
- **Track route files** are saved in app-private directories in formats such as JSON
- **Settings, cache, and free quota counters** (such as recent geocoding results) are stored on your device
- **Our servers do not store** your arrival records, tracks, photos, or complete location history by default

### 3.2 System Backup (Optional, Controlled by the System)

If you enable device system backup (such as iCloud, Google Backup, or manufacturer backup), data in the app-private directory may be included in the corresponding cloud backup service and is governed by that provider's policy. We **do not operate** a separate cloud business database; such backups are managed by you and your operating system provider.

### 3.3 iCloud Sync (Optional Future Feature)

If you choose to enable iCloud / CloudKit sync in a future version:

- Your data will be synced to the Apple ID account associated with your device through Apple's iCloud service
- Data transmission and storage are governed by Apple's Privacy Policy and security mechanisms
- Only you (and Apple ecosystem devices you authorize) can access your iCloud data
- We cannot directly read the contents of your iCloud account
- You can disable related sync at any time in system or app settings

### 3.4 Data Retention

- **Local data**: Remains on your device until you delete records or uninstall the App
- **Deleting data**: When you delete a record, we also delete associated local images and route files; uninstalling the App removes data in the app sandbox/private directory (images already saved to the photo library must be managed by you in Photos)
- **No default server backup**: Because we do not store your business data on our servers by default, there is generally no server-side retention period on our side

---

## 4. Information Sharing

### 4.1 We Do Not Proactively Share Your Business Data

Except as otherwise stated in this policy, we **will not** sell or proactively provide your arrival records, tracks, photos, or complete location history to third parties.

### 4.2 Third-Party Services

To provide certain features, your device may interact directly with the services below. These services have their own privacy policies:

#### 4.2.1 Apple System Services

- **Core Location**
  - **Purpose**: Obtain GPS altitude, coordinates, heading, and location permission status; background location updates may be enabled while track recording is in progress
  - **Data processing**: Processed locally on your device after authorization; geocoding and similar requests are handled by Apple services
  - **Your control**: You can manage location permissions in iOS Settings

- **WeatherKit (Weather, iOS)**
  - **Purpose**: Obtain current weather conditions and display Apple Weather attribution
  - **Data processing**: Requests are handled by Apple services
  - **Details**: Please see [Apple's Privacy Policy](https://www.apple.com/legal/privacy/)

- **Camera (AVFoundation / system camera capabilities)**
  - **Purpose**: Capture background photos for the summit camera
  - **Data processing**: Images are processed locally to generate cards; they are not automatically uploaded to our servers without your action
  - **Your control**: You can revoke camera permission in system settings at any time

- **Photo Library (Add Only)**
  - **Purpose**: Save generated summit/track cards to the system photo library
  - **Data processing**: Files are written directly to your device's photo library
  - **Your control**: You can revoke photo library write permission at any time

- **Motion and barometric sensors (Core Motion)**
  - **Purpose**: Read pressure and related data on supported devices
  - **Data processing**: Processed locally on the device
  - **Your control**: You can manage related permissions such as Motion & Fitness in system settings

- **Geocoding (CLGeocoder, etc.)**
  - **Purpose**: Convert coordinates into readable place names
  - **Data processing**: Requests are handled by the system or Apple services

- **StoreKit (In-App Purchases)**
  - **Purpose**: Purchase, verification, and restoration of Pro membership subscriptions and one-time purchases
  - **Data processing**: Payment and subscription management are handled by Apple; we only receive verified entitlement status

#### 4.2.2 Google and Android System Services

- **Fused Location Provider**
  - **Purpose**: Obtain GPS altitude, coordinates, and location permission status; during track recording, location is updated continuously in the background through a foreground service
  - **Data processing**: Processed locally on your device after authorization
  - **Your control**: You can manage location permissions in Android Settings → Apps → AltitudeNow → Permissions

- **Google Maps SDK**
  - **Purpose**: Track maps, Summit Passport map display, and route visualization
  - **Data processing**: Map tiles and related requests are handled by Google services
  - **Details**: Please see [Google's Privacy Policy](https://policies.google.com/privacy)

- **CameraX / system camera**
  - **Purpose**: Summit camera capture
  - **Data processing**: Images are processed locally on the device
  - **Your control**: You can revoke camera permission at any time

- **MediaStore (Photo Library)**
  - **Purpose**: Save cards to the system photo library (Android 10 and above usually requires no additional storage permission)
  - **Data processing**: Files are written to the device photo library

- **SensorManager**
  - **Purpose**: Barometer (if supported by the device), compass direction, and related sensors
  - **Data processing**: Processed locally on the device; related UI is hidden on devices without a barometer

- **Foreground service and notifications**
  - **Purpose**: Display persistent notifications such as "Recording track…" while track recording is in progress to maintain continuous location
  - **Data processing**: Notification content is used only to indicate recording status and does not include your track details

- **Google Play Billing (In-App Purchases)**
  - **Purpose**: Purchase, verification, and restoration of Pro membership subscriptions and one-time purchases
  - **Data processing**: Payment and subscription management are handled by Google; we only receive verified entitlement status

- **System Geocoder**
  - **Purpose**: Reverse geocoding to convert coordinates into place names

#### 4.2.3 Third-Party Weather Data (Open-Meteo)

- **Purpose**: Obtain weather codes and related information based on your approximate current location for on-screen or card display
- **Data processing**: Your device sends HTTPS requests to Open-Meteo, typically containing only latitude, longitude, and necessary query parameters; we do not operate this service and recommend reviewing [Open-Meteo's documentation](https://open-meteo.com/)
- **Note**: When the network is unavailable, the App may fall back to local rules for display without sending requests

#### 4.2.4 App Store Services

- **Apple App Store / Google Play**
  - **Purpose**: App distribution, version update queries, in-app purchases, and subscription management
  - **Data processing**: Handled by Apple or Google under their respective policies

#### 4.2.5 Sharing You Initiate

When you use the system Share feature, the destination apps you choose will handle the shared content under their own privacy policies. Sharing is initiated by you, and we are not responsible for how third-party apps process your data.

### 4.3 Legal Requirements

In rare cases, we may be required to disclose information:

- To comply with laws, regulations, legal processes, or government requests
- To protect our rights, property, or safety
- To prevent fraud or security threats
- To protect the lawful rights and interests of users or the public

Because we do not store your business data on our servers by default, we usually cannot provide data that has been deleted from your device or was never uploaded, even if we receive such a request; we will still cooperate within the scope permitted by law.

---

## 5. Data Security

### 5.1 Security Measures

We take the following measures to protect your information:

- **Local encryption and sandboxing**: Relying on each platform's data protection mechanisms, app data is stored in private spaces where other apps cannot access it directly
- **Minimum permissions**: Requesting only necessary permissions such as location, camera, photo library, sensors, and notifications when related features are used
- **No upload by default**: Arrival records, tracks, and photos remain on your device by default and are not routed through our servers
- **Secure development practices**: Following platform security recommendations and addressing known issues promptly

### 5.2 Your Responsibilities

To help protect your data, we recommend that you:

- Set a passcode or use biometric unlock on your device
- Do not share an unlocked device with others
- Keep your operating system updated to receive security patches
- Grant app permissions carefully and review permission settings regularly
- Before sharing cards in public, confirm whether they contain precise coordinates or place information you do not want to disclose

### 5.3 Data Breach Notification

Although we take reasonable measures, no system is completely secure. If a data security incident involving systems under our control occurs, we will:

- Investigate promptly and take remedial action
- Notify affected users within a reasonable time, where applicable
- Report to relevant regulators if required by law

---

## 6. Your Rights

### 6.1 Access and Control Over Your Data

You have control over your data:

- **View data**: Review historical data in Arrival Records, Track Records, and Summit Passport
- **Delete data**: Delete individual records by swiping or through in-app actions; deletion removes local database entries and associated image/route files
- **Export data**: Save summit/track cards to the photo library or export them through the system share feature

### 6.2 Revoking Permissions

You can revoke app permissions at any time in your device system settings. The exact path depends on your phone system, but you can usually find AltitudeNow in Settings and manage location, camera, photo library, notifications, motion & fitness, and related permissions. Track recording may require separate authorization for background location on some systems. Revoking permissions may make related features unavailable or degraded (for example, without location permission, real-time altitude or track recording cannot work).

### 6.3 Deleting Account and Data

This App does not require account registration. You can delete data by:

- **Deleting records**: Deleting individual or all arrival/track records in the App
- **Deleting the App**: Uninstalling the App removes data in the app-private directory
- **Photo library content**: Images saved to the system photo library must be deleted in the Photos app
- **iCloud data**: If iCloud sync is enabled in the future, manage the corresponding data in iCloud or Apple ID settings
- **Subscription management**: Pro membership subscriptions can be canceled in the app store account settings where you made the purchase; **Pro benefits purchased through different channels do not automatically carry over**

---

## 7. Children's Privacy

AltitudeNow is intended for general users. We do not knowingly collect personal information from children under 13.

If you are a parent or guardian and believe your child has provided us with personal information without your consent, please contact us and we will take steps to delete the relevant information.

---

## 8. International Users

AltitudeNow can be used in different regions (actual availability depends on app stores and regional policies). If you use this App outside mainland China:

- Your business data is stored locally on your device by default
- If iCloud sync (future feature) or system backup is enabled, data storage location depends on your account region and the relevant provider's service layout
- We strive to follow core principles of applicable data protection laws (such as GDPR and CCPA); specific rights may vary by local law

---

## 9. Changes to This Privacy Policy

### 9.1 Update Notice

We may update this Privacy Policy from time to time to reflect:

- Changes in app features (such as subscriptions, iCloud sync, etc.)
- Legal and regulatory requirements
- User feedback and best practices

### 9.2 How We Will Notify You

When we make material changes to this Privacy Policy, we will:

- Display a notice in the app
- Update the "Last Updated" date at the top of this document
- Describe the changes in the app store release notes

### 9.3 Your Choices

If you do not agree with the updated Privacy Policy, you may:

- Stop using the App
- Delete the App and your data
- Contact us to express your concerns

Continued use of the App means you accept the updated Privacy Policy.

---

## 10. Contact Us

If you have any questions, comments, or complaints about this Privacy Policy, please contact us:

**Email**: tenthproducts@zohomail.cn

**Response time**: We will reply within 7 business days after receiving your email.

We value your feedback and are committed to addressing your privacy concerns.

---

## 11. Governing Law

This Privacy Policy is governed by the laws of the People's Republic of China (excluding its conflict-of-law rules).

If you have any dispute regarding our privacy practices, we encourage you to contact us first using the information above. If the dispute cannot be resolved through friendly negotiation, you agree to submit it to the competent people's court where we are located.

---

## 12. Other Important Information

### 12.1 Data Minimization

We follow the principle of data minimization and collect or process only information necessary to provide the service, prioritizing processing on your device.

### 12.2 Transparency Commitment

We are committed to transparency in data processing and clearly explain permission purposes, local storage, and network-related steps in this policy.

### 12.3 User Trust

Your trust is our most valuable asset. We will continue working to balance "summit moments worth sharing" with privacy-friendly design.

---

**Thank you for choosing AltitudeNow!**

We are committed to helping you record every arrival with confidence and leaving the choice of whether to share entirely up to you.

---

*The AltitudeNow development team reserves the right of final interpretation of this Privacy Policy.*
