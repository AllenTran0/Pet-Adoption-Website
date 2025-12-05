import React, { createContext, useState, useContext, ReactNode } from "react";

type SettingsType = {
  dark_mode: boolean;
  text_size: number;
  image_size: number;
  high_contrast: boolean;
  updateSetting: (key: keyof SettingsType, value: boolean | number) => void;
};

const defaultSettings: SettingsType = {
  dark_mode: false,
  text_size: 0,
  image_size: 0,
  high_contrast: false,
  updateSetting: () => {},
};

const Settingsimport = createContext<SettingsType>(defaultSettings);

export const SettingsProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [settings, setSettings] = useState<Omit<SettingsType, "updateSetting">>({
    dark_mode: false,
    text_size: 0,
    image_size: 0,
    high_contrast: false,
  });

  const updateSetting = (key: keyof SettingsType, value: boolean | number) => {
    setSettings((prev) => ({ ...prev, [key]: value }));
  };

  return (
    <Settingsimport.Provider value={{ ...settings, updateSetting }}>
      {children}
    </Settingsimport.Provider>
  );
};

export const useSettings = () => useContext(Settingsimport);
