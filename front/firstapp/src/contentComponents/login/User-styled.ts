import styled from "styled-components";


interface UserStyledProps {
  valid: boolean;

}


export const UserStyled = styled.div`
  font-size: 20px;
  border-radius: inherit;
  padding: 5px;
  border: 2px solid ${(p: UserStyledProps) => p.valid ? 'blue' : 'red'};
`