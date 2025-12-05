import "bootstrap/dist/css/bootstrap.min.css";
import "../styles/Settings.css"
import { useState, useEffect } from "react";

// Define TypeScript Interfaces
interface SettingsData {
  dark_mode: boolean;
  text_size: number;  // 0 for small, 1 for medium, 2 for large
  image_size: number; // 0 for small, 1 for medium, 2 for large
  high_contrast: boolean;
}



// Mapping for size display
const sizeLabels = ["Small", "Medium", "Large"];

// Define text sizes for each label
const textSizeStyles = {
  0: { fontSize: "0.8em" },  // Small
  1: { fontSize: "1em" },    // Medium
  2: { fontSize: "1.2em" },  // Large
};

export const Settings = () => {
  // Initialize state with default settings
  const [settings, setSettings] = useState<SettingsData>({
    dark_mode: false,
    text_size: 1, // Medium
    image_size: 1, // Medium
    high_contrast: false,
  });
  const rootElement = document.getElementById("root");
  if (settings.dark_mode) {
    rootElement.classList.add("dark-mode");
    if (settings.high_contrast) {
      rootElement.classList.add("high-contrast");
    } else {
      rootElement.classList.remove("high-contrast");
    }
  } else {
    rootElement.classList.remove("dark-mode", "high-contrast");
  }


  // Fetch settings from backend on mount
  useEffect(() => {
    const fetchSettings = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5001/settings_get");
        if (!response.ok) {
          throw new Error("Failed to fetch settings");
        }
        const data = await response.json();

        // Normalize the data from backend
        setSettings({
          dark_mode: data.dark_mode === "1" || data.dark_mode === true,
          text_size: data.text_size,
          image_size: data.image_size,
          high_contrast: data.high_contrast === "1" || data.high_contrast === true,
        });
      } catch (error) {
        console.error("Error fetching settings:", error);
      }
    };
    fetchSettings();
  }, []);

  // Function to handle updates to individual settings
  const handleUpdateSetting = (key: keyof SettingsData, value: boolean | number) => {
    setSettings((prevSettings) => ({
      ...prevSettings,
      [key]: value,
    }));
  };

  // Function to post settings to backend
  const postSettings = () => {
    const options = {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        dark_mode: settings.dark_mode ? "True" : "False",
        text_size: settings.text_size,
        image_size: settings.image_size,
        high_contrast: settings.high_contrast ? "True" : "False",
      }),
    };
  
    fetch('http://127.0.0.1:5001/settings_post', options)
      .then((response) => {
        console.log("Request Sent:", options);
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Something went wrong ...');
        }
      })
      .then((data) => console.log("Settings Updated:", data))
      .catch((error) => console.error("Error:", error));
  };
  
  

  // Inline styles with dynamic text size
  const styles = {
    settingsContainer: {
      padding: "20px",
      backgroundColor: settings.dark_mode
        ? settings.high_contrast
          ? "#000" // True black for high contrast
          : "#333" // Dark gray for regular dark mode
        : "#fff", // White for light mode
      color: settings.dark_mode
        ? settings.high_contrast
          ? "#fff" // True white for high contrast
          : "#ddd" // Light gray for regular dark mode
        : "#000", // Black for light mode
    },
    settingsTitle: {
      fontSize: "2em",
      fontWeight: "bold",
      ...textSizeStyles[settings.text_size], // Dynamic font size
    },
    iconBar: {
      width: "5px",
      height: "40px",
      backgroundColor: settings.dark_mode
        ? settings.high_contrast
          ? "#fff" // White for high contrast
          : "#aaa" // Light gray for regular dark mode
        : "#1f1f1f", // Dark gray for light mode
      marginRight: "10px",
      borderRadius: "5px",
    },
    settingsIcon: {
      width: "30px",
      height: "30px",
      marginLeft: "10px",
    },
    settingsDescription: {
      fontSize: "0.9em",
      color: settings.dark_mode
        ? settings.high_contrast
          ? "#fff" // High-contrast text
          : "#ccc" // Regular dark mode text
        : "#666", // Light mode text
      marginTop: "10px",
    },
    settingsLabel: {
      fontSize: "1.2em",
      fontWeight: "bold",
      marginRight: "15px",
      ...textSizeStyles[settings.text_size], // Dynamic font size
      color: settings.dark_mode
        ? settings.high_contrast
          ? "#fff" // High-contrast text
          : "#ddd" // Regular dark mode text
        : "#000", // Light mode text
    },
    settingsSection: {
      display: "flex",
      alignItems: "center",
      marginTop: "20px",
    },
    btnGroupBtn: {
      width: "80px",
      backgroundColor: settings.dark_mode
        ? settings.high_contrast
          ? "#222" // Darker gray for high contrast
          : "#444" // Regular dark mode button background
        : "#fff", // Light mode button background
      color: settings.dark_mode
        ? settings.high_contrast
          ? "#fff" // High-contrast text color
          : "#ddd" // Regular dark mode text
        : "#000", // Light mode text color
    },
  };

  return (
    <div style={styles.settingsContainer}>
      <h1 style={styles.settingsTitle}>
        <span style={styles.iconBar}></span>
        Settings
        <img src="/settings.png" alt="Settings Icon" style={styles.settingsIcon} />
      </h1>

     {/* Text Size Settings */}
<div className="settings-section">
  <span className="icon-bar"></span>
  <p className="settings-label">Text Size</p>
  <div className="btn-group" role="group" aria-label="Text Size">
    {sizeLabels.map((label, index) => (
      <button
        key={index}
        type="button"
        className={`btn ${
          settings.text_size === index ? "btn-active" : "btn-inactive"
        }`}
        onClick={() => handleUpdateSetting("text_size", index)}
      >
        {label}
      </button>
    ))}
  </div>
</div>

{/* Image Size Settings */}
<div className="settings-section">
  <span className="icon-bar"></span>
  <p className="settings-label">Image Size</p>
  <div className="btn-group" role="group" aria-label="Image Size">
    {sizeLabels.map((label, index) => (
      <button
        key={index}
        type="button"
        className={`btn ${
          settings.image_size === index ? "btn-active" : "btn-inactive"
        }`}
        onClick={() => handleUpdateSetting("image_size", index)}
      >
        {label}
      </button>
    ))}
  </div>
</div>


      {/* High Contrast Settings */}
      <div style={styles.settingsSection}>
        <span style={styles.iconBar}></span>
        <p style={styles.settingsLabel}>High Contrast</p>
        <div className="form-check form-switch">
          <input
            className="form-check-input"
            type="checkbox"
            role="switch"
            id="highContrastSwitch"
            checked={settings.high_contrast}
            onChange={() => handleUpdateSetting("high_contrast", !settings.high_contrast)}
          />
        </div>
      </div>
      <p style={styles.settingsDescription}>
        Enhances the visibility of text and elements by using stark color differences between the foreground and background.
      </p>

      {/* Dark Mode Settings */}
      <div style={styles.settingsSection}>
        <span style={styles.iconBar}></span>
        <p style={styles.settingsLabel}>Dark Mode</p>
        <div className="form-check form-switch">
          <input
            className="form-check-input"
            type="checkbox"
            role="switch"
            id="darkModeSwitch"
            checked={settings.dark_mode}
            onChange={() => handleUpdateSetting("dark_mode", !settings.dark_mode)}
          />
        </div>
      </div>

      {/* Save Settings Button */}
      <button onClick={postSettings} style={{ marginTop: "20px" }} className="btn btn-primary">
        Save Settings
      </button>
    </div>
  );
};