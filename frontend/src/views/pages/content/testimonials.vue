<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <testimonialsheader :title="title" :text="text" />

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
                    <template v-if="column.key === 'name'">
                      <h2 class="table-avatar d-flex">
                        <router-link to="/profile" class="avatar avatar-md me-2"><img class="avatar-img rounded-circle"
                            :src="require(`@/assets/img/profiles/${record.img}`)" alt="User Image" /></router-link>
                        <router-link to="/profile">{{ record.UserName
                        }}<span>{{ record.mail }}</span></router-link>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'id'">
                      <span class="mail-important"><i class="fas fa-star starred text-warning ms-1"></i></span>
                      <span class="mail-important"><i class="fas fa-star starred text-warning ms-1"></i></span>
                      <span class="mail-important"><i class="fas fa-star starred text-warning ms-1"></i></span>
                      <span class="mail-important"><i class="fas fa-star starred text-warning ms-1"></i></span>
                      <span class="mail-important"><i class="fas fa-star starred text-warning ms-1"></i></span>
                    </template>
                    <template v-else-if="column.key === 'status'">
                      <span class="badge badge-pill bg-success-light" v-if="record.Status == 'Active'">{{ record.Status
                      }}</span>
                      <span class="badge badge-pill bg-danger-light" v-else-if="record.Status == 'Deactive'">{{
                        record.Status }}</span>
                    </template>
                    <template v-else-if="column.key === 'action'">
                      <div class="d-flex align-items-center">
                        <a class="btn-action-icon me-2" href="javascript:void(0);" data-bs-toggle="modal"
                          data-bs-target="#edit_testimonial"><i class="feather feather-edit"></i></a>
                        <a class="btn-action-icon" href="javascript:void(0);" data-bs-toggle="modal"
                          data-bs-target="#delete_modal"><i class="feather feather-trash-2"></i></a>
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

  <testimonialsmodel></testimonialsmodel>
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
    key: "name",
    sorter: {
      compare: (a, b) => {
        a = a.UserName.toLowerCase();
        b = b.UserName.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Rating",
    dataIndex: "Rating",
    key: "id",
    sorter: true,
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
    title: "Status",
    dataIndex: "Status",
    key: "status",
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
    NUM: "1",
    UserName: "John Smith",
    img: "avatar-14.jpg",
    mail: "john@example.com",
    Content: "Lorem ipsum dolor sit amet, consectetur",
    CreatedOn: "19 Dec 2023, 06:12 PM",
    Status: "Active",
  },
  {
    NUM: "2",
    UserName: "Johnny",
    img: "avatar-15.jpg",
    mail: "johnny@example.com",
    Content: "Lorem ipsum dolor sit amet, consectetur",
    CreatedOn: "15 Dec 2023, 06:12 PM",
    Status: "Active",
  },
  {
    NUM: "3",
    UserName: "Robert",
    img: "avatar-16.jpg",
    mail: "robert@example.com",
    Content: "Lorem ipsum dolor sit amet, consectetur",
    CreatedOn: "04 Dec 2023, 12:38 PM",
    Status: "Deactive",
  },
  {
    NUM: "4",
    UserName: "Sharonda",
    img: "avatar-17.jpg",
    mail: "sharon@example.com",
    Content: "Lorem ipsum dolor sit amet, consectetur",
    CreatedOn: "14 Dec 2023, 12:38 PM",
    Status: "Active",
  },
  {
    NUM: "5",
    UserName: "Pricilla",
    img: "avatar-18.jpg",
    mail: "pricilla@example.com",
    Content: "Lorem ipsum dolor sit amet, consectetur",
    CreatedOn: "12 Dec 2023, 12:38 PM",
    Status: "Active",
  },
  {
    NUM: "6",
    UserName: "Randall",
    img: "avatar-19.jpg",
    mail: "randall@example.com",
    Content: "Lorem ipsum dolor sit amet, consectetur",
    CreatedOn: "04 Dec 2023, 12:38 PM",
    Status: "Deactive",
  },
];
export default {
  setup() {
    return {
      title: "Testimonials",
      text: "Add Testimonials",
      data,
      columns,
    };
  },
};
</script>
