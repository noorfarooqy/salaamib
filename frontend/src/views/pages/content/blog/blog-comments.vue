<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <blogcommentsheader :title="title" />

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

      <!-- Table -->
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
                          <span>{{ record.Phonenumber }}</span></router-link>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'action'">
                      <a class="btn-action-icon" href="javascript:void(0);" download=""><i
                          class="feather feather-trash-2"></i></a>
                    </template>
                  </template>
                </a-table>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Table -->
    </div>
  </div>
  <!-- /Page Wrapper -->
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
    title: "Email",
    dataIndex: "Email",
    sorter: {
      compare: (a, b) => {
        a = a.Email.toLowerCase();
        b = b.Email.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Content",
    dataIndex: "Content",
    sorter: {
      compare: (a, b) => {
        a = a.Content.toLowerCase();
        b = b.Content.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Created On",
    dataIndex: "CreatedOn",
    sorter: {
      compare: (a, b) => {
        a = a.CreatedOn.toLowerCase();
        b = b.CreatedOn.toLowerCase();
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
    NUM: "1",
    img: "avatar-14.jpg",
    UserName: "John Smith",
    Phonenumber: "+1 843-443-3282",
    Email: "john@example.com",
    Content: "Lorem ipsum dolor sit amet, consectetur",
    CreatedOn: "19 Dec 2023, 06:12 PM",
  },
  {
    NUM: "2",
    img: "avatar-15.jpg",
    UserName: "Johnny",
    Phonenumber: "+1 917-409-0861",
    Email: "johnny@example.com",
    Content: "Excepteur sint occaecat cupidatat non",
    CreatedOn: "15 Dec 2023, 04:35 PM",
  },
  {
    NUM: "3",
    img: "avatar-16.jpg",
    UserName: "Robert",
    Phonenumber: "+1 956-623-2880",
    Email: "robert@example.com",
    Content: "Duis aute irure dolor in reprehenderit",
    CreatedOn: "04 Dec 2023, 12:38 PM",
  },
  {
    NUM: "4",
    img: "avatar-17.jpg",
    UserName: "Sharonda",
    Phonenumber: "+1 707-439-1732",
    Email: "sharon@example.com",
    Content: "Excepteur sint occaecat cupidatat non",
    CreatedOn: "14 Dec 2023, 12:38 PM",
  },
  {
    NUM: "5",
    img: "avatar-18.jpg",
    UserName: "Pricilla",
    Phonenumber: "+1 707-439-1732",
    Email: "pricilla@example.com",
    Content: "Sed ut perspiciatis unde omnis iste natus",
    CreatedOn: "12 Dec 2023, 12:38 PM",
  },
  {
    NUM: "6",
    img: "avatar-19.jpg",
    UserName: "Randall",
    Phonenumber: "+1 707-439-1732",
    Email: "randall@example.com",
    Content: "Neque porro quisquam est, qui dolorem ipsum",
    CreatedOn: "04 Dec 2023, 12:38 PM",
  },
];
export default {
  data() {
    return {
      title: "Blog Comments",
      data,
      columns,
    };
  },
};
</script>
