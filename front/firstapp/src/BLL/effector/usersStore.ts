import {createEffect, createEvent, createStore} from 'effector'
import {db} from "../../DAL/firebase/firebaseInit";
import {collection, getDocs} from "firebase/firestore";


export interface User {
    name: string | null
}


export const checkUser = createEvent<User>()
const addUser = createEvent<User>()

//стор на хранение ссылки

export const saveUsername = createEvent<string>()



export const $currentUsername = createStore('').on(
    saveUsername, (state, userName) => {
        return userName
    })









