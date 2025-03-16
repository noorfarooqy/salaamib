const earningsChart = {
  series: [
    {
      name: "Earnings ",
      colors: ["#7539FF"],
      data: [
        {
          x: "Jan",
          y: 40,
        },
        {
          x: "Feb",
          y: 38,
        },
        {
          x: "Mar",
          y: 50,
        },
        {
          x: "Apr",
          y: 85,
        },
        {
          x: "May",
          y: 55,
        },
        {
          x: "Jun",
          y: 45,
        },
        {
          x: "Jul",
          y: 60,
        },
        {
          x: "Aug",
          y: 40,
        },
        {
          x: "Sep",
          y: 43,
        },
        {
          x: "Oct",
          y: 30,
        },
        {
          x: "Nov",
          y: 65,
        },
        {
          x: "Dec",
          y: 50,
        },
      ],
    },
  ],
  chart: {
    type: "bar",
    height: 250,
    plotOptions: {
      bar: {
        borderRadiusApplication: "around",
      },
    },
    dataLabels: {
      enabled: false,
    },
    colors: ["#7539FF"],
    xaxis: {
      type: "category",
      group: {
        style: {
          fontSize: "7px",
          fontWeight: 700,
        },
      },
    },
  },
};

const planeChart = {
  series: [
    {
      data: [400, 325, 312, 294, 254, 252],
    },
  ],
  chart: {
    type: "bar",
    height: 300,

    plotOptions: {
      bar: {
        barHeight: "100%",
        distributed: true,
        horizontal: true,
      },
    },
    colors: ["#FFEFDD", "#EADDFF", "#DDF3FF", "#FFECEC", "#E1FFED", "#E0E0E0"],
    dataLabels: {
      enabled: true,
      textAnchor: "end",
      margin: 10,
      style: {
        colors: ["#1D1D1D"],
      },
      formatter: function (val, opt) {
        return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val;
      },
      offsetX: 0,
      dropShadow: {
        enabled: true,
      },
    },
    stroke: {
      width: 0,
      colors: ["#1D1D1D"],
    },
    xaxis: {
      categories: [
        "Sales : $6,100,00",
        "Sales : $5,100,00",
        "Sales : $4,200,00",
        "Sales : $3,400,00",
        "Sales : $3,400,00",
        "Sales : $400,00",
      ],
    },
    yaxis: {
      labels: {
        show: false,
      },
    },
    tooltip: {
      theme: "dark",
      x: {
        show: false,
      },
      y: {
        title: {
          formatter: function () {
            return "";
          },
        },
      },
    },
  },
};

const companiesFlow = {
  series: [
    {
      name: "Companies",
      data: [25, 40, 30, 55, 25, 35, 25, 50, 20],
    },
  ],
  chart: {
    height: 273,
    type: "area",
    zoom: {
      enabled: false,
    },
    colors: ["#FF9F43"],
  dataLabels: {
    enabled: false,
  },
  stroke: {
    curve: "straight",
  },
  title: {
    text: "",
    align: "left",
  },
  xaxis: {
    categories: ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"],
  },
  yaxis: {
    min: 10,
    max: 60,
    tickAmount: 5,
    labels: {
      formatter: (val) => {
        return val / 1 + "K";
      },
    },
  },
  legend: {
    position: "top",
    horizontalAlign: "left",
  },
  },
};

export { earningsChart, planeChart, companiesFlow };
