# AltitudeNow Privacy Policy

**Effective Date: September 14, 2026**

**Last Updated: September 14, 2026**

---

## Introduction

Welcome to AltitudeNow!

This Privacy Policy applies to the AltitudeNow service you use (the "Mini Program" or "Service"). The Service is provided as a WeChat Mini Program and may use WeChat open capabilities such as location, camera, photo library, maps, and cloud development.

We understand that your privacy matters. We are committed to handling your information in a transparent and restrained manner, and to keeping your data on your device whenever possible. This Privacy Policy is designed to help you understand:

- What information we collect
- How we use that information
- Your control over your information
- How we protect your information

Please read this Privacy Policy carefully. By using the Mini Program, you agree to the practices described in this policy. You must also comply with WeChat Mini Program privacy guidelines and related platform rules.

---

## 1. Information We Collect

### 1.1 Information We Collect or Process

This Mini Program processes data on a "local-first, minimum necessary" basis. We may collect or process the following information:

#### 1.1.1 Information You Provide or That Is Generated Through Use

- **Location and altitude information**: After you grant WeChat location permission (`scope.userLocation`), we use APIs such as `wx.getLocation` / `wx.startLocationUpdate` to read GPS coordinates, altitude (if supported by the device), accuracy, and related data to display real-time altitude, resolve place names, generate summit cards, compute session activity metrics (distance / elevation gain / duration), and display the Summit Passport
- **Photos and images**: When you use the summit camera (`<camera>` component) or mark an arrival with a theme background Pin, the Mini Program captures or generates images; summit cards may include your photos plus overlaid text and graphics
- **Arrival record data**: Including capture or save time, altitude, latitude and longitude, place text, selected template, activity metrics (such as distance, elevation gain, and duration), and local image file paths
- **Summit Passport data**: Visit point information (coordinates, etc.) aggregated on your device from local summit records for map Pin display; this data is derived from on-device records and is not uploaded to our own servers by default
- **Mini Program settings**: Such as altitude units (meters/feet), language preference, haptic feedback toggle, summit theme colors, and other preferences stored on your device

#### 1.1.2 Automatically Collected Information

- **Device and sensor information**: Features such as the compass may read device orientation sensor data (for example via `wx.startCompass`); such data is processed locally and is not uploaded to our servers by default. The current version generally does not rely on a barometer; if related displays are added later, this policy will be updated
- **Basic runtime information**: To keep the Mini Program running properly, we may obtain basic technical information through WeChat interfaces such as system type, base library version, Mini Program version, and language/region settings (for compatibility checks and bug fixes, and not to identify a specific natural person)
- **WeChat platform identifiers**: If cloud development or cloud functions are used (for example as a reverse-geocoding proxy), WeChat may provide technical identifiers needed for the session (such as openid for calling cloud functions); we **do not** use them to build advertising profiles, and we **do not require** authorization of avatar, nickname, or similar user profile information

#### 1.1.3 Information Processed Over the Network (Not Stored on Our Own Business Servers by Default)

In the following scenarios, some data may leave your device, but **we do not use it to build user profiles on our own servers or to store your personal movement history long term**:

- **Reverse geocoding**: To convert coordinates into place names, latitude and longitude may be forwarded via a WeChat cloud function to geocoding APIs such as **Tencent Location Services**; this processing is governed by Tencent's and WeChat's privacy policies; the cloud function acts as a proxy with necessary short-term caching and is not intended for long-term retention of personal movement profiles
- **Map services**: Summit Passport and related features may use the WeChat `<map>` component (Tencent Map capabilities); during map loading your device or the WeChat client may communicate with map services (such as map tile requests), which may involve approximate location information
- **Weather queries (if enabled later)**: If a future version integrates third-party weather data, requests typically contain only approximate latitude and longitude and necessary query parameters; this policy will be updated before such features go live

### 1.2 Information We Do Not Collect

Except when you contact us directly, we **do not proactively collect** the following:

- Your name, national ID number, bank account details, or other strong identity identifiers
- Your contacts, SMS messages, or call logs
- Your WeChat Pay password or other account credentials
- Advertising identifiers used for cross-app tracking (this Mini Program is not designed for ad tracking)
- **Track recording data**: This Mini Program does **not** provide track recording, track record lists, or continuous background track location
- **Payment and subscription information**: The current version does **not** integrate membership subscriptions or in-app payments and does not collect payment card numbers or other financial information
- A separate self-built account or independent cloud business data backup (the current version requires no separate registration; summit records are stored in the local WeChat Mini Program storage by default)

---

## 2. How We Use Information

### 2.1 How We Use Your Information

Information we collect or process is used only for the following purposes:

#### 2.1.1 Providing Core Features

- **Real-time altitude and place display**: Using location and altitude data to show your current status on the summit screen
- **Compass (if available)**: Displaying bearing, latitude and longitude, and current altitude
- **Summit camera and card generation**: Combining photos or theme backgrounds with altitude, place, time, and other information into shareable cards (the current version does not force a watermark by default)
- **Arrival records**: Saving, displaying, and managing your historical summit records locally on your device
- **Summit Passport**: Aggregating and displaying Pins for places you have visited based on local summit records
- **Export and sharing**: Saving cards to the system photo library when authorized, or letting you choose recipients through WeChat sharing
- **Settings and units**: Remembering your units, language, and related preferences

#### 2.1.2 Improving the Service Experience

- **Performance and compatibility**: Analyzing necessary diagnostic and version information to improve stability
- **Bug fixes**: Collecting necessary diagnostic information to resolve defects quickly
- **Feature improvement**: Understanding feature usage (if anonymous analytics services are integrated in the future, this policy will be updated accordingly)

### 2.2 How We Will Not Use Your Information

We promise that we will **not**:

- Sell, rent, or trade your personal information to third parties
- Use your arrival records or photos for unauthorized advertising
- Share personally identifiable information with other companies or organizations (except as required by law or with your explicit consent)
- Use your data for purposes not described in this policy without notice

---

## 3. Information Storage

### 3.1 Local Storage

This Mini Program uses a **local-first** data storage strategy:

- **Arrival records and related metadata** are stored in WeChat Mini Program local storage (such as `wx.setStorage`)
- **Summit card images** are saved in the Mini Program user file directory (such as `wx.env.USER_DATA_PATH`) and/or in the system photo library if you choose to save them there
- **Settings and cache** (such as recent geocoding results) are stored on your device
- **Our own business servers do not store** your arrival records, photos, or complete location history by default

### 3.2 Cloud Functions and Optional Cloud Development

If cloud functions are enabled to proxy reverse geocoding or similar capabilities:

- Request parameters such as latitude and longitude may briefly pass through the cloud function runtime
- We may use short-term caching to reduce duplicate requests; **we do not retain long-term business copies for the purpose of building your personal movement profile**
- The cloud environment is provided by platforms such as WeChat Cloud Development and is governed by WeChat's service terms and privacy policies

### 3.3 Cross-Device Sync

The current version does **not** provide cross-device cloud sync. Your summit records remain in this device's Mini Program storage by default.

### 3.4 Data Retention

- **Local data**: Remains on your device until you delete records or clear Mini Program data / remove the Mini Program
- **Deleting data**: When you delete a record, we also delete associated local images; clearing Mini Program data or deleting the Mini Program removes business data in local storage (images already saved to the photo library must be managed by you in Photos)
- **No default business backup on our servers**: Because we do not store your summit records on our own business servers by default, there is generally no server-side retention period on our side

---

## 4. Information Sharing

### 4.1 We Do Not Proactively Share Your Business Data

Except as otherwise stated in this policy, we **will not** sell or proactively provide your arrival records, photos, or complete location history to third parties.

### 4.2 Third-Party Services

To provide certain features, your device or the WeChat client may interact directly with the services below. These services have their own privacy policies:

#### 4.2.1 WeChat Open Capabilities and System Permissions

- **Location (`scope.userLocation`)**
  - **Purpose**: Obtain GPS altitude, coordinates, and location permission status; support session activity metrics and Passport display
  - **Data processing**: Used for on-device display and local records after authorization; this Mini Program does not provide continuous background track location for track recording
  - **Your control**: You can manage location permission in WeChat Settings → Privacy / Mini Program permissions or in system settings, and via `wx.openSetting`

- **Camera (`scope.camera`)**
  - **Purpose**: Capture background photos for the summit camera; theme Pin mode may not require the camera
  - **Data processing**: Images are processed on-device to generate cards; they are not automatically uploaded to our own servers without your action
  - **Your control**: You can revoke camera permission at any time

- **Save to Photos (`scope.writePhotosAlbum`)**
  - **Purpose**: Save generated summit cards to the system photo library
  - **Data processing**: Files are written to your device photo library; authorization is requested on first save as required by WeChat
  - **Your control**: You can revoke photo library write permission at any time

- **Sharing**
  - **Purpose**: Share cards or Mini Program pages with friends or group chats through the WeChat share menu or share button
  - **Data processing**: Sharing is initiated by you; content is handled by WeChat and recipients under their rules

- **Feedback and similar open capabilities (if used)**
  - **Purpose**: For example `button open-type="feedback"` to help you report issues
  - **Data processing**: Governed by the corresponding WeChat capability rules

#### 4.2.2 Tencent Location / Map Related Services

- **Reverse geocoding (Tencent Location Services, via cloud function proxy)**
  - **Purpose**: Convert coordinates into readable place names
  - **Data processing**: Requests may include latitude and longitude; processed by Tencent Location Services, with cloud functions used to hide API keys and proxy calls
  - **Details**: Please see the [Tencent Privacy Policy](https://www.tencent.com/en-us/privacy-policy.html) and related WeChat documentation

- **Map component (`<map>` / Tencent Map capabilities)**
  - **Purpose**: Summit Passport map display and Pin visualization
  - **Data processing**: Map tiles and related requests are handled by Tencent Map / WeChat map capabilities and may involve approximate location information

#### 4.2.3 WeChat Platform

- **Purpose**: Mini Program distribution, runtime, cloud development (if enabled), and basic security/compliance capabilities
- **Data processing**: Handled by Tencent / WeChat under their privacy policies and Mini Program platform rules

#### 4.2.4 Sharing You Initiate

When you share content to WeChat friends, group chats, or other scenes, recipients and WeChat will handle the shared content under their respective rules. Sharing is initiated by you, and we are not responsible for subsequent third-party processing.

### 4.3 Legal Requirements

In rare cases, we may be required to disclose information:

- To comply with laws, regulations, legal processes, or government requests
- To protect our rights, property, or safety
- To prevent fraud or security threats
- To protect the lawful rights and interests of users or the public

Because we do not store your summit records on our own business servers by default, we usually cannot provide data that has been deleted from your device or was never uploaded, even if we receive such a request; we will still cooperate within the scope permitted by law.

---

## 5. Data Security

### 5.1 Security Measures

We take the following measures to protect your information:

- **Local-first and sandboxing**: Relying on WeChat Mini Program storage and file sandbox mechanisms, business data is kept in the Mini Program's private space
- **Minimum permissions**: Requesting only necessary permissions such as location, camera, and photo library when related features are used
- **Key protection**: Third-party API keys for reverse geocoding are proxied through cloud functions and are not hardcoded in the client
- **No upload of business data by default**: Arrival records and photos remain on your device by default and are not routed through our own business servers
- **Secure development practices**: Following WeChat Mini Program security recommendations and addressing known issues promptly

### 5.2 Your Responsibilities

To help protect your data, we recommend that you:

- Set a lock screen passcode or use biometric unlock on your phone
- Do not share an unlocked device that is signed in to WeChat
- Keep the WeChat client and operating system updated
- Grant Mini Program permissions carefully and review permission lists regularly in WeChat settings
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

- **View data**: Review historical data in Records and Summit Passport
- **Delete data**: Delete individual records through in-Mini Program actions; deletion removes local storage entries and associated images
- **Export data**: Save summit cards to the photo library or export them through WeChat sharing

### 6.2 Revoking Permissions and Privacy Authorization

You can revoke permissions granted to this Mini Program (location, camera, photo library, etc.) at any time in WeChat or system settings. Revoking permissions may make related features unavailable or degraded (for example, without location permission, real-time altitude cannot work).

You may also manage privacy authorization for this Mini Program under WeChat Mini Program privacy guidelines; if you refuse authorization, we will only provide features that do not depend on the corresponding permissions, or explain the functional limitation.

### 6.3 Deleting Data

This Mini Program does not require a separate account registration. You can delete data by:

- **Deleting records**: Deleting individual or all arrival records in the Mini Program
- **Clearing Mini Program data / deleting the Mini Program**: Removes business data in local storage and the user file directory
- **Photo library content**: Images saved to the system photo library must be deleted in the Photos app

---

## 7. Children's Privacy

This Mini Program is intended for general users. We do not knowingly collect personal information from children under 13.

If you are a parent or guardian and believe your child has provided us with personal information without your consent, please contact us and we will take steps to delete the relevant information.

---

## 8. Regions and Scope

This Service is provided as a WeChat Mini Program; actual availability depends on WeChat's regional openness and category review policies. If you use this Mini Program outside mainland China:

- Your business data is stored locally on your device (WeChat Mini Program storage) by default
- Tencent Location, Maps, Cloud Development, and similar services may be unavailable depending on region or account environment; related features may be hidden or degraded when unavailable
- We strive to follow core principles of applicable data protection laws; specific rights may vary by local law

---

## 9. Changes to This Privacy Policy

### 9.1 Update Notice

We may update this Privacy Policy from time to time to reflect:

- Changes in Mini Program features (such as weather, analytics services, cloud sync, etc.)
- Legal and regulatory requirements and WeChat platform rules
- User feedback and best practices

### 9.2 How We Will Notify You

When we make material changes to this Privacy Policy, we will:

- Display a notice in the Mini Program or update the privacy guidelines
- Update the "Last Updated" date at the top of this document
- Describe the changes in release notes where applicable

### 9.3 Your Choices

If you do not agree with the updated Privacy Policy, you may:

- Stop using the Mini Program
- Delete the Mini Program and clear related data
- Contact us to express your concerns

Continued use of the Mini Program means you accept the updated Privacy Policy.

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

We are committed to transparency in data processing and clearly explain permission purposes, local storage, and network-related steps in this policy (including location, camera, photo library, Tencent Location/Maps, and cloud function proxies).

### 12.3 User Trust

Your trust is our most valuable asset. We will continue working to balance "summit moments worth sharing" with privacy-friendly design.

---

**Thank you for choosing AltitudeNow!**

We are committed to helping you record every arrival with confidence and leaving the choice of whether to share entirely up to you.

---

*The AltitudeNow development team reserves the right of final interpretation of this Privacy Policy.*
