<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <userheader :title="title" :text="text" />

      <!-- Search Filter -->
      <userfilter></userfilter>
      <!-- /Search Filter -->

      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'id'">
                      <h2 class="table-avatar d-flex">
                        <router-link to="/profile" class="avatar avatar-sm me-2"><img class="avatar-img rounded-circle"
                            :src="require(`@/assets/img/profiles/${record.img}`)" alt="User Image" /></router-link>
                        <router-link to="/profile">{{ record.UserName }}
                          <span>{{ record.mail }}</span></router-link>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'LastActivity'">
                      <span class="badge badge-pill bg-ash-gray text-gray-light"
                        v-if="record.LastActivity === '10 mins ago'">{{ record.LastActivity }}</span>
                      <span class="badge badge-pill bg-ash-gray text-gray-light"
                        v-else-if="record.LastActivity === '2 days ago'">{{ record.LastActivity }}</span>
                      <span class="badge badge-pill bg-ash-gray text-gray-light"
                        v-else-if="record.LastActivity === '1 hour ago'">{{ record.LastActivity }}</span>
                      <span class="badge badge-pill bg-success-light" v-else-if="record.LastActivity === 'Online'">{{
                        record.LastActivity }}</span>
                    </template>
                    <template v-else-if="column.key === 'Status'">
                      <span class="badge badge-pill bg-success-light" v-if="record.Status === 'Active'">{{ record.Status
                      }}</span>
                      <span class="badge badge-pill bg-ash-gray text-gray-light"
                        v-else-if="record.Status === 'Restricted'">{{ record.Status }}</span>
                    </template>
                    <template v-else-if="column.key === 'action'">
                      <div class="d-flex align-items-center">
                        <div class="dropdown dropdown-action">
                          <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown"
                            aria-expanded="false"><i class="fas fa-ellipsis-v"></i></a>
                          <div class="dropdown-menu dropdown-menu-right">
                            <ul>
                              <li>
                                <a class="dropdown-item" href="javascript:void(0);" data-bs-toggle="modal"
                                  data-bs-target="#edit_user"><i class="far fa-edit me-2"></i>Edit</a>
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
  <usermodel></usermodel>
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
    title: "User Name",
    dataIndex: "UserName",
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.UserName.toLowerCase();
        b = b.UserName.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Mobile Number",
    dataIndex: "MobileNumber",
    sorter: {
      compare: (a, b) => {
        a = a.MobileNumber.toLowerCase();
        b = b.MobileNumber.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Role",
    dataIndex: "Role",
    sorter: {
      compare: (a, b) => {
        a = a.Role.toLowerCase();
        b = b.Role.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Last Activity",
    dataIndex: "LastActivity",
    key: "LastActivity",
    sorter: {
      compare: (a, b) => {
        a = a.LastActivity.toLowerCase();
        b = b.LastActivity.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Created on",
    dataIndex: "Createdon",
    sorter: {
      compare: (a, b) => {
        a = a.Createdon.toLowerCase();
        b = b.Createdon.toLowerCase();
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
    key: "action",
    sorter: true,
  },
];
const data = [
  {
    id: "1",
    img: "avatar-14.jpg",
    UserName: "John Smith",
    mail: "john@example.com",
    MobileNumber: "+1 989-438-3131",
    Role: "$4,220",
    LastActivity: "10 mins ago",
    Createdon: "19 Dec 2022, 06:12 PM",
    class: "badge bg-ash-gray text-gray-light",
    class1: "badge  bg-success-light",
    Status: "Active",
  },
  {
    id: "2",
    img: "avatar-15.jpg",
    UserName: "Johnny",
    mail: "johnny@example.com",
    MobileNumber: "+1 843-443-3282",
    Role: "$1,862",
    LastActivity: "Online",
    Createdon: "15 Dec 2022, 06:12 PM",
    class: "badge  bg-success-light",
    class1: "badge  bg-success-light",
    Status: "Active",
  },
  {
    id: "3",
    img: "avatar-16.jpg",
    UserName: "Robert",
    mail: "robert@example.com",
    MobileNumber: "+1 917-409-0861",
    Role: "$2,789",
    LastActivity: "Online",
    Createdon: "04 Dec 2022, 12:38 PM",
    class: "badge  bg-success-light",
    class1: "badge  bg-ash-gray text-gray-light",
    Status: "Restricted",
  },
  {
    id: "4",
    img: "avatar-17.jpg",
    UserName: "Sharonda",
    mail: "sharon@example.com",
    MobileNumber: "+1 956-623-2880",
    Role: "$6,789",
    LastActivity: "1 hour ago",
    Createdon: "14 Dec 2022, 12:38 PM",
    class: "badge bg-ash-gray text-gray-light",
    class1: "badge  bg-success-light",
    Status: "Active",
  },
  {
    id: "5",
    img: "avatar-18.jpg",
    UserName: "Pricilla",
    mail: "pricilla@example.com",
    MobileNumber: "+1 956-613-2880",
    Role: "$1,789",
    LastActivity: "Online",
    Createdon: "12 Dec 2022, 12:38 PM",
    class: "badge  bg-success-light",
    class1: "badge  bg-success-light",
    Status: "Active",
  },
  {
    id: "6",
    img: "avatar-19.jpg",
    UserName: "Randall",
    mail: "randall@example.com",
    MobileNumber: "+1 117-409-0861",
    Role: "$1,789",
    LastActivity: "2 days ago",
    Createdon: "04 Dec 2022, 12:38 PM",
    class: "badge bg-ash-gray text-gray-light",
    class1: "badge  bg-ash-gray text-gray-light",
    Status: "Restricted",
  },
];

export default {
  data() {
    return {
      title: "Users",
      text: "Add User",
      data,
      columns,
    };
  },
};
</script>
