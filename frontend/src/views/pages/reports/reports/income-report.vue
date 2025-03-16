<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <paymentreport-header :title="title" />
      <!-- /Page Header -->

      <!-- Search Filter -->
      <div id="filter_inputs" class="card filter-card">
        <div class="card-body pb-0">
          <div class="row">
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Name</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Email</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Phone</label>
                <input type="text" class="form-control" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Search Filter -->

      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'Company'">
                      <h2 class="table-avatar d-flex">
                        <router-link to="/profile" class="avatar avatar-md me-2"><img class="avatar-img rounded-circle"
                            :src="require(`@/assets/img/profiles/${record.Image}`)" alt="User Image" /></router-link>
                        <router-link to="/profile">{{ record.Company }}
                          <span>{{ record.Email }}</span></router-link>
                      </h2>
                    </template>
                  </template>
                </a-table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <incomemodel></incomemodel>
</template>
<script>
const columns = [
  {
    title: "#",
    dataIndex: "id",
    sorter: {
      compare: (a, b) => {
        a = a.id.toLowerCase();
        b = b.id.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },

  {
    title: "Company",
    dataIndex: "Company",
    key: "Company",
    sorter: {
      compare: (a, b) => {
        a = a.Company.toLowerCase();
        b = b.Company.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Date",
    dataIndex: "Date",
    sorter: {
      compare: (a, b) => {
        a = a.Date.toLowerCase();
        b = b.Date.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Income Amount",
    dataIndex: "IncomeAmount",
    sorter: {
      compare: (a, b) => {
        a = a.IncomeAmount.toLowerCase();
        b = b.IncomeAmount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Payment Method",
    dataIndex: "PaymentMethod",
    sorter: {
      compare: (a, b) => {
        a = a.PaymentMethod.toLowerCase();
        b = b.PaymentMethod.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  }
];
const data = [
  {
    id: "1",
    Image: "avatar-14.jpg",
    Company: "Orn LLC",
    Email: "orn@example.com",
    IncomeAmount: "$2000.00",
    PaymentMethod: "Cash",
    Date: "20 Sep 2023",
  },
  {
    id: "2",
    Image: "avatar-15.jpg",
    Company: "Accent Technology",
    Email: "accent@example.com",
    IncomeAmount: "$0.00",
    PaymentMethod: "Cash",
    Date: "15 Sep 2023",
  },
  {
    id: "3",
    Image: "avatar-15.jpg",
    Company: "Express Advertising",
    Email: "express@example.com",
    IncomeAmount: "$1009.00",
    PaymentMethod: "Cash",
    Date: "10 Sep 2023",
  },
  {
    id: "4",
    Image: "avatar-16.jpg",
    Company: "Lexicon Technologies",
    Email: "lexicon@example.com",
    IncomeAmount: "$1500.00",
    PaymentMethod: "Cash",
    Date: "05 Aug 2023",
  },
  {
    id: "5",
    Image: "avatar-17.jpg",
    Company: "Sumo Soft Limited",
    Email: "sumo@example.com",
    IncomeAmount: "$1000.00",
    PaymentMethod: "Cash",
    Date: "01 July 2023",
  },
];
export default {
  data() {
    return {
      title: "Income Report",
      data,
      columns,
    };
  },
};
</script>
