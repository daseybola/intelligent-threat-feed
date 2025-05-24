import axios from 'axios';

export const fetchThreats = async () => {
  const response = await axios.get("http://localhost:8000/threats");
  return response.data;
};
