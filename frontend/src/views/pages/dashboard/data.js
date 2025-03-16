const scolAreaChart = {
  scol: {
    chart: {
      id: "vuechart-example",
      type: "bar",
      fontFamily: "Poppins, sans-serif",
      height: 350,
      toolbar: {
        show: false,
      },
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: "60%",
        endingShape: "rounded",
      },
    },
    colors: ["#7638ff", "#fda600"],
    dataLabels: {
      enabled: false,
    },
    stroke: {
      show: true,
      width: 2,
      colors: ["transparent"],
    },
    xaxis: {
      categories: [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
      ],
    },
    yaxis: {
      title: {
        text: "$ (thousands)",
      },
    },
    fill: {
      opacity: 1,
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return "$ " + val + " thousands";
        },
      },
    },
  },
  series: [
    {
      name: "Received",
      type: "column",
      data: [70, 150, 80, 180, 150, 175, 201, 60, 200, 120, 190, 160, 50],
    },
    {
      name: "Pending",
      type: "column",
      data: [23, 42, 35, 27, 43, 22, 17, 31, 22, 22, 12, 16, 80],
    },
  ],
};

const donutAreaCharts = {
  donutchart: {
    chart: {
      id: "vuechart-example",
      fontFamily: "Poppins, sans-serif",
      height: 320,
      type: "donut",
    },
  },
  colors: ["#7638ff", "#ff737b", "#fda600", "#1ec1b0"],
  series: [55, 40, 20, 10],
  dataLabels: {
    enabled: false,
  },
  labels: ["Paid", "Unpaid", "Overdue", "Draft"],
  legend: { show: false },
  responsive: [
    {
      breakpoint: 480,
      options: {
        chart: {
          width: 200,
          height: 200,
        },
        legend: {
          position: "bottom",
        },
      },
    },
  ],
};
export { scolAreaChart, donutAreaCharts };
