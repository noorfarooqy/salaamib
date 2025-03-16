<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <customerheader />

      <!-- Search Filter -->
      <div id="filter_inputs" class="card filter-card">
        <div class="card-body pb-0">
          <div class="row">
            <div class="col-sm-6 col-md-3">
              <div class="form-group">
                <label>Name</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="form-group">
                <label>Email</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="form-group">
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
                    <template v-if="column.key === 'Name'">
                      <h2 class="table-avatar d-flex">
                        <router-link to="/profile" class="avatar avatar-md me-2"><img class="avatar-img rounded-circle"
                            :src="require(`@/assets/img/profiles/${record.Image}`)" alt="User Image" /></router-link>
                        <router-link to="/profile">{{ record.Name }}<span>{{ record.Email }}</span></router-link>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'Status'">
                      <span :class="record.Class">{{ record.Status }}</span>
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="d-flex align-items-center">
                        <router-link to="/invoices/add-invoice" class="btn btn-greys me-2"><i
                            class="fa fa-plus-circle me-1"></i> Invoice</router-link>
                        <router-link to="customers-ledger" class="btn btn-greys me-2"><i
                            class="fa-regular fa-eye me-1"></i> Ledger</router-link>
                        <div class="dropdown dropdown-action">
                          <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown"
                            aria-expanded="false"><i class="fas fa-ellipsis-v"></i></a>
                          <div class="dropdown-menu dropdown-menu-end">
                            <ul>
                              <li>
                                <router-link class="dropdown-item" to="/customers/edit-customer"><i
                                    class="far fa-edit me-2"></i>Edit</router-link>
                              </li>
                              <li>
                                <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                  data-bs-target="#delete_modal"><i class="far fa-trash-alt me-2"></i>Delete</a>
                              </li>
                              <li>
                                <router-link class="dropdown-item" to="customer-details"><i
                                    class="far fa-eye me-2"></i>View</router-link>
                              </li>
                              <li>
                                <router-link class="dropdown-item" to="active-customers"><i
                                    class="far fa-bell me-2"></i>Active</router-link>
                              </li>
                              <li>
                                <router-link class="dropdown-item" to="deactive-customers"><i
                                    class="far fa-bell-slash me-2"></i>Deactivate</router-link>
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
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
  <locationmodal :Delete="Delete" />
</template>

<script>
const columns = [
  {
    title: "#",
    dataIndex: "NUM",
    sorter: {
      compare: (a, b) => {
        a = a.NUM.toLowerCase();
        b = b.NUM.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Name",
    dataIndex: "Name",
    key: "Name",
    sorter: {
      compare: (a, b) => {
        a = a.Name.toLowerCase();
        b = b.Name.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Phone",
    dataIndex: "Phone",
    sorter: {
      compare: (a, b) => {
        a = a.Phone.toLowerCase();
        b = b.Phone.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Balance",
    dataIndex: "Balance",
    sorter: {
      compare: (a, b) => {
        a = a.Balance.toLowerCase();
        b = b.Balance.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "TotalInvoice",
    dataIndex: "TotalInvoice",
    sorter: {
      compare: (a, b) => {
        a = a.TotalInvoice.toLowerCase();
        b = b.TotalInvoice.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Created",
    dataIndex: "Created",
    sorter: {
      compare: (a, b) => {
        a = a.Created.toLowerCase();
        b = b.Created.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Status",
    dataIndex: "Status",
    key: "Status",
    sorter: {
      compare: (a, b) => {
        a = a.Status.toLowerCase();
        b = b.Status.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Action",
    key: "Action",
    sorter: true,
  },
];
const data = [
  {
    NUM: "1",
    Image: "avatar-14.jpg",
    Name: "John Smith",
    Email: "john@example.com",
    Phone: "+1 989-438-3131",
    Balance: "$4,220",
    TotalInvoice: "2",
    Created: "19 Dec 2023, 06:12 PM",
    Class: "badge badge-pill bg-success-light",
    Status: "Active",
  },
  {
    NUM: "2",
    Image: "avatar-15.jpg",
    Name: "Johnny Charles",
    Email: "johnny@example.com",
    Phone: "+1 843-443-3282",
    Balance: "$1,862",
    TotalInvoice: "1",
    Created: "15 Dec 2023, 06:12 PM",
    Class: "badge badge-pill bg-success-light",
    Status: "Active",
  },
  {
    NUM: "3",
    Image: "avatar-16.jpg",
    Name: "Robert George",
    Email: "robert@example.com",
    Phone: "+1 917-409-0861",
    Balance: "$2,789",
    TotalInvoice: "3",
    Created: "04 Dec 2023, 12:38 PM",
    Class: "badge badge-pill bg-danger-light",
    Status: "Deactive",
  },
  {
    NUM: "4",
    Image: "avatar-17.jpg",
    Name: "Sharonda Letha ",
    Email: "sharon@example.com",
    Phone: "+1 956-623-2880",
    Balance: "$6,789",
    TotalInvoice: "6",
    Created: "14 Dec 2023, 12:38 PM",
    Class: "badge badge-pill bg-success-light",
    Status: "Active",
  },
  {
    NUM: "5",
    Image: "avatar-18.jpg",
    Name: "Pricilla Maureen",
    Email: "pricilla@example.com",
    Phone: "+1 956-613-2880",
    Balance: "$1,789",
    TotalInvoice: "4",
    Created: "12 Dec 2023, 12:38 PM",
    Class: "badge badge-pill bg-success-light",
    Status: "Active",
  },
  {
    NUM: "6",
    Image: "avatar-19.jpg",
    Name: "Randall Hollis",
    Email: "randall@example.com",
    Phone: "+1 117-409-0861",
    Balance: "$1,789",
    TotalInvoice: "1",
    Created: "04 Dec 2023, 12:38 PM",
    Class: "badge badge-pill bg-danger-light",
    Status: "Deactive",
  },
];

export default {
  data() {
    return {
      title1: "Delete FAQ",
      Delete: "Delete Customer",
      columns,
      data,
    };
  },
};
</script>
