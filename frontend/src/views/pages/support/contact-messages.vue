<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <supportheader :title="title" />
      <!-- Table -->
      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'id'">
                      <h2 class="table-avatar d-flex align-items-center">
                        <router-link to="/contact-details" class="avatar avatar-sm me-2"><img
                            class="avatar-img rounded-circle" :src="require('@/assets/img/profiles/' + record.img)"
                            alt="User Image" /></router-link>
                        <router-link to="/profile">{{ record.Name }}</router-link>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'action'">
                      <div class="d-flex align-items-center">
                        <a class="btn-action-icon me-2" href="javascript:void(0);" data-bs-toggle="modal"
                          data-bs-target="#edit_contact"><i class="feather feather-edit"></i></a>
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
      <!-- /Table -->
    </div>
  </div>
  <!-- /Page Wrapper -->
  <ticketmodal></ticketmodal>
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
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.Name.toLowerCase();
        b = b.Name.toLowerCase();
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
    title: "Message",
    dataIndex: "Message",
    sorter: {
      compare: (a, b) => {
        a = a.Message.toLowerCase();
        b = b.Message.toLowerCase();
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
    title: "Action",
    key: "action",
    class: "text-end",
    sorter: true,
  },
];
const data = [
  {
    NUM: "1",
    img: "avatar-14.jpg",
    Name: "John Smith",
    Email: "john@example.com",
    MobileNumber: "+1 989-438-3131",
    Message: "Lorem ipsum dolor sit consectetur",
    Createdon: "19 Dec 2023, 06:12 PM",
  },
  {
    NUM: "2",
    img: "avatar-15.jpg",
    Name: "Johnny",
    Email: "johnny@example.com",
    MobileNumber: "+1 843-443-3282",
    Message: "Ut enim ad minim veniam, quis",
    Createdon: "15 Dec 2023, 04:35 PM",
  },
  {
    NUM: "3",
    img: "avatar-16.jpg",
    Name: "Robert",
    Email: "robert@example.com",
    MobileNumber: "+1 917-409-0861",
    Message: "Duis aute irure dolor in reprehenderit",
    Createdon: "04 Dec 2023, 04:35 PM",
  },
  {
    NUM: "4",
    img: "avatar-17.jpg",
    Name: "Sharonda",
    Email: "sharon@example.com",
    MobileNumber: "+1 956-623-2880",
    Message: "Excepteur sint occaecat cupidatat",
    Createdon: "12 Dec 2023, 04:35 PM",
  },
  {
    NUM: "5",
    img: "avatar-18.jpg",
    Name: "Randall",
    Email: "randall@example.com",
    MobileNumber: "+1 707-439-1732",
    Message: "Sed ut perspiciatis unde omnis iste",
    Createdon: "28 Nov 2023, 03:25 PM",
  },
  {
    NUM: "6",
    img: "avatar-19.jpg",
    Name: "Pricilla",
    Email: "pricilla@example.com",
    MobileNumber: "+1 559-741-9672",
    Message: "Nemo enim ipsam voluptatem quia",
    Createdon: "15 Nov 2023, 03:25 PM",
  },
];
export default {
  setup() {
    return {
      title: "Contact Messages",
      data,
      columns,
    };
  },
};
</script>
