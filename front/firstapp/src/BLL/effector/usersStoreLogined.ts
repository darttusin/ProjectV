import {createEffect, createEvent, createStore} from 'effector'
import {User} from "./usersStore";

//создание ивента с дженерик User - определение типа
export const deleteUser = createEvent()

export const rememberUser = createEvent<User>()

export const currentUser = createStore<User>({name: null})
    .on(rememberUser, (state, payload) => {
        return payload
    })




