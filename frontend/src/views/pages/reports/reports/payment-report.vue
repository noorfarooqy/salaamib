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
                <a-table
                  class="stripped table-hover"
                  :columns="columns"
                  :data-source="data"
                >
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'Company'">
                      <h2 class="table-avatar d-flex">
                        <router-link to="/profile" class="avatar avatar-md me-2"
                          ><img
                            class="avatar-img rounded-circle"
                            :src="require(`@/assets/img/profiles/${record.Image}`)"
                            alt="User Image"
                        /></router-link>
                        <router-link to="/profile"
                          >{{ record.Company }}
                          <span>{{ record.Email }}</span></router-link
                        >
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
  <paymentmodel></paymentmodel>
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
    title: "Payment Received",
    dataIndex: "PaymentReceived",
    sorter: {
      compare: (a, b) => {
        a = a.PaymentReceived.toLowerCase();
        b = b.PaymentReceived.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Payment Send",
    dataIndex: "PaymentSend",
    sorter: {
      compare: (a, b) => {
        a = a.PaymentSend.toLowerCase();
        b = b.PaymentSend.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Net Payment",
    dataIndex: "NetPayment",
    sorter: {
      compare: (a, b) => {
        a = a.NetPayment.toLowerCase();
        b = b.NetPayment.toLowerCase();
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
    PaymentSend: "$500.00",
    NetPayment: "$1500.00",
    PaymentReceived: "$2000.00",
  },
  {
    id: "2",
    Image: "avatar-15.jpg",
    Company: "Accent Technology",
    Email: "accent@example.com",
    PaymentSend: "$0.00",
    NetPayment: "$1000.00",
    PaymentReceived: "$1000.00",
  },
  {
    id: "3",
    Image: "avatar-15.jpg",
    Company: "Express Advertising",
    Email: "express@example.com",
    PaymentSend: "$100.00",
    NetPayment: "$100.00",
    PaymentReceived: "$200.00",
  },
  {
    id: "4",
    Image: "avatar-16.jpg",
    Company: "Lexicon Technologies",
    Email: "lexicon@example.com",
    PaymentSend: "$1500.00",
    NetPayment: "$3500.00",
    PaymentReceived: "$5000.00",
  },
  {
    id: "5",
    Image: "avatar-17.jpg",
    Company: "Sumo Soft Limited",
    Email: "sumo@example.com",
    PaymentSend: "$1000.00",
    NetPayment: "$2000.00",
    PaymentReceived: "$3000.00",
  },
];
export default {
  data() {
    return {
      title: "Payment Report",
      data,
      columns,
    };
  },
};
</script>
