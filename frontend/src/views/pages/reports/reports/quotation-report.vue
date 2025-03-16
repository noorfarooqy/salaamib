<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>

  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <quotationreport-header :title="title" />
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
                        <router-link to="/profile" class="avatar avatar-md me-2"
                          ><img
                            class="avatar-img rounded-circle"
                            :src="require(`@/assets/img/profiles/${record.Image}`)"
                            alt="User Image"
                        /></router-link>
                        <router-link to="/profile"
                          >{{ record.CompanyName }}
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
  <quotationreportmodal></quotationreportmodal>
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
    title: "Serial Number",
    dataIndex: "SerialNumber",
    sorter: {
      compare: (a, b) => {
        a = a.SerialNumber.toLowerCase();
        b = b.SerialNumber.toLowerCase();
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
    title: "Company Name",
    dataIndex: "CompanyName",
    key: "CompanyName",
    sorter: {
      compare: (a, b) => {
        a = a.CompanyName.toLowerCase();
        b = b.CompanyName.toLowerCase();
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
    title: "Due Date",
    dataIndex: "DueDate",
    sorter: {
      compare: (a, b) => {
        a = a.DueDate.toLowerCase();
        b = b.DueDate.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  }
];
const data = [
  {
    id: "1",
    SerialNumber: "AA1100123",
    Image: "avatar-14.jpg",
    Date: "01 Aug 2023, 04:35 PM",
    CompanyName: "Orn LLC",
    Email: "orn@example.com",
    Amount: "$199.99",
    DueDate: "20 Aug 2023",
  },
  {
    id: "2",
    SerialNumber: "AA1100123",
    Image: "avatar-15.jpg",
    Date: "05 Aug 2023, 07:00 PM",
    CompanyName: "Accent Technology",
    Email: "accent@example.com",
    Amount: "$99.99",
    DueDate: "23 Aug 2023",
  },
  {
    id: "3",
    SerialNumber: "AA1100123",
    Image: "avatar-15.jpg",
    Date: "13 Aug 2023, 06:35 PM",
    CompanyName: "Express Advertising",
    Email: "express@example.com",
    Amount: "300.00",
    DueDate: "24 Aug 2023",
  },
  {
    id: "4",
    SerialNumber: "AA1100123",
    Image: "avatar-16.jpg",
    Date: "15 Aug 2023, 03:30 PM",
    CompanyName: "Lexicon Technologies",
    Email: "lexicon@example.com",
    Amount: "690.00",
    DueDate: "25 Aug 2023",
  },
  {
    id: "5",
    SerialNumber: "AA1100123",
    Image: "avatar-17.jpg",
    Date: "16 Aug 2023, 05:15 PM",
    CompanyName: "Sumo Soft Limited",
    Email: "sumo@example.com",
    Amount: "$99.99",
    DueDate: "30 Aug 2023",
  },
];
export default {
  data() {
    return {
      title: "Quotation Report",
      data,
      columns,
    };
  },
};
</script>
