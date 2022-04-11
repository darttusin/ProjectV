import styled from "styled-components";

interface LoginStyledProps {
    valid?: boolean;
}

export const LoginStyled = styled.div`
  display: flex;
  flex-direction: column;
  width: 43%;
  justify-content: space-between;
  background-color: azure;
  border-radius: 7px;
  border: 2px solid ${(p: LoginStyledProps) => p.valid ? 'deepskyblue' : 'red'};
  /*border: 1px solid #001529;*/ 
  padding: 35px 20px 35px 20px;
  height: 75%;
  
`