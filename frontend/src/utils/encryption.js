import CryptoJS from 'crypto-js';

// In Vue CLI, environment variables are accessed through process.env
const ENCRYPTION_KEY = process.env.VUE_APP_ENCRYPTION_KEY || 'fallback-dev-key';

export const encryptData = (data) => {
  try {
    if (!data) return null;
    const jsonString = JSON.stringify(data);
    return CryptoJS.AES.encrypt(jsonString, ENCRYPTION_KEY).toString();
  } catch (error) {
    console.error('Encryption error:', error);
    return null;
  }
};

export const decryptData = (encryptedData) => {
  try {
    if (!encryptedData) return null;
    const bytes = CryptoJS.AES.decrypt(encryptedData, ENCRYPTION_KEY);
    const decryptedString = bytes.toString(CryptoJS.enc.Utf8);
    return JSON.parse(decryptedString);
  } catch (error) {
    console.error('Decryption error:', error);
    return null;
  }
}; 