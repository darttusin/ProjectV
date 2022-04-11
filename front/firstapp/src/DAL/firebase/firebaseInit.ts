// Import the functions you need from the SDKs you need

import {initializeApp} from "firebase/app"
import {getFirestore} from "firebase/firestore"
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyARxIozsOX2T8LJ_L2dC2KLTnV1ntMLFSE",
    authDomain: "firstproject-eefb6.firebaseapp.com",
    projectId: "firstproject-eefb6",
    storageBucket: "firstproject-eefb6.appspot.com",
    messagingSenderId: "188437669889",
    appId: "1:188437669889:web:54a6dc9a0fcba93e9fb800",
    measurementId: "G-WXXPFHNSJ8"
};

const firebaseApp = initializeApp(firebaseConfig);

// Initialize Firebase
export const db = getFirestore()
