import React, {useState} from 'react';
import '../App.css';
import {TextStyled} from '../styledComponent/TextStyled';
import {Input} from 'antd';
import {LoginStyled} from "./Login-styled";
import {UserStyled} from "./login/User-styled";
import {UserAllStyled} from "./login/UserAll-styled";
import {ButtonFilledStyled} from '../styledComponent/ButtonFilled-styled';
import {ButtonStyled} from '../styledComponent/Button-styled';
import {
    $currentUsername,
    saveUsername,
} from "../BLL/effector/usersStore";
import {useStore} from "effector-react";
import {InputFilledStyled} from '../styledComponent/InputFilled-styled';
import {useHistory} from "react-router-dom";

const Upload: React.FC = () => {
    const username = useStore($currentUsername)



    const history = useHistory();


    const [isValid, setValid] = useState(true)


    //сохранение ссылки в сторе
    const handleUsernameChange = (e: { target: { value: React.SetStateAction<string> } }) => {
        saveUsername(e.target.value as string)
    }
    
    const isStringValid = (string: string): boolean => {
        const res = /^[A-Za-z0-9_\./-?=+!:]/.exec(string);
        return !!res;
    }

    const checkUserRegistered = () => {
        history.push('/home')
    };

    const upload = () => {
        history.push('/home')
    }

// вместо checkuserregistered вставаить ссыль на процесс ссылки на видео
    return (
        <LoginStyled valid={isValid}>
            <InputFilledStyled justifycontent={"space-between"} width={100} height={100}>
                <UserAllStyled>
                    <UserStyled valid={isStringValid(username)}>
                        <TextStyled textSize={20} color={'black'} fontWeight={"bold"}>
                            Paste your link here
                        </TextStyled>
                        <Input value={username} onChange={handleUsernameChange}/>
                    </UserStyled>
                </UserAllStyled>
                    <ButtonStyled onClick={checkUserRegistered}> 
                        To process
                    </ButtonStyled>
            </InputFilledStyled>

            <ButtonFilledStyled width={100} height={30} justifycontent={'center'}>
                <ButtonStyled onClick={upload}>
                    Upload
                </ButtonStyled>

            </ButtonFilledStyled>
        </LoginStyled>

        
    )
}

export default Upload;
