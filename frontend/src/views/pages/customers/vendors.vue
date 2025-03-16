<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <vendorsheader />

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
                        <router-link to="/profile" class="avatar avatar-sm me-2"><img class="avatar-img rounded-circle"
                            :src="require(`@/assets/img/profiles/${record.Image}`)" alt="User Image" /></router-link>
                        <router-link to="/profile">{{ record.Name }}<span>{{ record.Email }}</span></router-link>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="d-flex align-items-center">
                        <router-link to="ledger" class="btn btn-greys me-2"><i class="fa fa-eye me-1"></i>
                          Ledger</router-link>
                        <div class="dropdown dropdown-action text-end">
                          <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown"
                            aria-expanded="false"><i class="fas fa-ellipsis-v"></i></a>
                          <div class="dropdown-menu dropdown-menu-end">
                            <ul>
                              <li>
                                <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                  data-bs-target="#edit_vendor"><i class="far fa-edit me-2"></i>Edit</a>
                              </li>
                              <li>
                                <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                  data-bs-target="#delete_modal"><i class="far fa-trash-alt me-2"></i>Delete</a>
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

  <!-- /Page Wrapper -->
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
    title: "Action",
    key: "Action",
    sorter: true,
    class: "text-center",
  },
];
const data = [
  {
    NUM: 1,
    Image: "avatar-14.jpg",
    Name: "John Smith",
    Email: "john@example.com",
    Phone: "+1 989-438-3131",
    Created: "19 Dec 2022, 06:12 PM",
    Balance: "$4,220",
  },
  {
    NUM: 2,
    Image: "avatar-15.jpg",
    Name: "Johnny",
    Email: " johnny@example.com",
    Phone: "+1 843-443-3282",
    Created: "15 Dec 2022, 06:12 PM",
    Balance: "$1,862",
  },
  {
    NUM: 3,
    Image: "avatar-16.jpg",
    Name: "Robert",
    Email: " robert@example.com",
    Phone: "+1 917-409-0861",
    Created: "04 Dec 2022, 12:38 PM",
    Balance: "$2,789",
  },
  {
    NUM: 4,
    Image: "avatar-17.jpg",
    Name: "Sharonda",
    Email: " sharon@example.com",
    Phone: "+1 956-623-2880",
    Created: "14 Dec 2022, 12:38 PM",
    Balance: "$6,789",
  },
  {
    NUM: 5,
    Image: "avatar-18.jpg",
    Name: "Pricilla ",
    Email: "pricilla@example.com",
    Phone: "+1 956-613-2880",
    Created: "12 Dec 2022, 12:38 PM",
    Balance: "$1,789",
  },
  {
    NUM: 6,
    Image: "avatar-19.jpg",
    Name: "Randall ",
    Email: "randall@example.com",
    Phone: "+1 117-409-0861",
    Created: "04 Dec 2022, 12:38 PM",
    Balance: "$1,789",
  },
];
export default {
  data() {
    return {
      Delete: "Delete Vendor",
      columns,
      data,
    };
  },
};
</script>
