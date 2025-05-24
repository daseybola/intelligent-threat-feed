import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import { fetchThreats } from '../api';
import { Chart as ChartJS, BarElement, CategoryScale, LinearScale } from 'chart.js';

ChartJS.register(BarElement, CategoryScale, LinearScale);

export default function Dashboard() {
  const [threats, setThreats] = useState([]);

  useEffect(() => {
    fetchThreats().then(setThreats);
  }, []);

  const scores = threats.map(t => t.score);
  const labels = threats.map((t, i) => `Threat ${i + 1}`);
  const chartData = {
    labels,
    datasets: [{
      label: 'Threat Scores',
      data: scores,
      backgroundColor: 'rgba(255, 99, 132, 0.6)',
    }]
  };

  return (
    <div>
      <h2>Threat Score Chart</h2>
      <Bar data={chartData} />
    </div>
  );
}
