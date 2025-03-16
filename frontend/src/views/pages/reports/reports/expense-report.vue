<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>

  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <reportheader :title="title" />
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
                    <template v-if="column.key === 'CompanyName'">
                      <h2 class="table-avatar d-flex">
                        <router-link to="/contact-details" class="avatar avatar-md me-2"
                          ><img
                            class="avatar-img rounded-circle"
                            :src="require(`@/assets/img/profiles/${record.Image}`)"
                            alt="User Image"
                        /></router-link>
                        <router-link to="/profile"
                          >{{ record.Name }}<span>{{ record.Email }}</span></router-link
                        >
                      </h2>
                    </template>
                    <template v-if="column.key === 'PaymentStatus'">
                      <span :class="record.class">{{ record.PaymentStatus }}</span>
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
  <expensemodel></expensemodel>
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
    title: "Company Name",
    dataIndex: "Name",
    key: "CompanyName",
    sorter: {
      compare: (a, b) => {
        a = a.Name.toLowerCase();
        b = b.Name.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Amount",
    dataIndex: "Amount",
    sorter: {
      compare: (a, b) => {
        a = a.Amount.toLowerCase();
        b = b.Amount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Payment Status",
    dataIndex: "PaymentStatus",
    key: "PaymentStatus",
    sorter: {
      compare: (a, b) => {
        a = a.PaymentStatus.toLowerCase();
        b = b.PaymentStatus.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Category",
    dataIndex: "Category",
    key: "Category",
    sorter: {
      compare: (a, b) => {
        a = a.Category.toLowerCase();
        b = b.Category.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Created By",
    dataIndex: "CreatedBy",
    sorter: {
      compare: (a, b) => {
        a = a.CreatedBy.toLowerCase();
        b = b.CreatedBy.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  }
];
const data = [
  {
    id: "1",
    Image: "avatar-14.jpg",
    Email: "orn@example.com",
    Name: "Orn LLC",
    PaymentStatus: "Paid",
    CreatedBy: "01 Aug 2023, 04:35 PM",
    class: "badge bg-success-light text-success-light",
    Category: "Marketing",
    Amount: "$199.99",
  },
  {
    id: "2",
    Image: "avatar-15.jpg",
    Email: "accent@example.com",
    Name: "Accent Technology",
    PaymentStatus: "Paid",
    CreatedBy: "05 Aug 2023, 07:00 PM",
    class: "badge bg-success-light text-success-light",
    Category: "Software",
    Amount: "$99.99",
  },
  {
    id: "3",
    Image: "avatar-16.jpg",
    Email: "express@example.com",
    Name: "Express Advertising",
    PaymentStatus: "Paid",
    CreatedBy: "13 Aug 2023, 06:35 PM",
    class: "badge bg-success-light text-success-light",
    Category: "Advertising",
    Amount: "$300.00",
  },
  {
    id: "4",
    Image: "avatar-17.jpg",
    Email: "lexicon@example.com",
    Name: "Lexicon Technologies ",
    PaymentStatus: "Pending",
    CreatedBy: "15 Aug 2023, 03:30 PM",
    class: "badge bg-warning-light text-warning-light",
    Category: "Software",
    Amount: "$690.00",
  },
  {
    id: "5",
    Image: "avatar-18.jpg",
    Email: "sumo@example.com",
    Name: "Sumo Soft Limited",
    PaymentStatus: "Pending",
    CreatedBy: "16 Aug 2023, 05:15 PM",
    class: "badge bg-warning-light text-warning-light",
    Category: "Stationery",
    Amount: "$99.99",
  },
];
export default {
  data() {
    return {
      title: "Expense Report",
      data,
      columns,
    };
  },
};
</script>
