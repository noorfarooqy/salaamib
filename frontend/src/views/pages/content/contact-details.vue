<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <div class="page-header">
        <div class="content-page-header">
          <h5>Contact Details</h5>
        </div>
      </div>

      <ul class="contact-details">
        <li>
          <div class="d-flex align-items-center">
            <span class="me-3"><img class="rounded-circle" width="38" height="38"
                src="@/assets/img/profiles/avatar-14.jpg" alt="User Image" /></span>
            <div>
              <p>John Smith</p>
              <span>john@example.com</span>
            </div>
          </div>
        </li>
        <li>
          <div class="d-flex align-items-center">
            <span class="contact-square d-flex align-items-center justify-content-center rounded-circle">
              <i class="feather feather-mail"></i>
            </span>
            <div>
              <p>Email</p>
              <span>john@example.com</span>
            </div>
          </div>
        </li>
        <li>
          <div class="d-flex align-items-center">
            <span class="contact-square d-flex align-items-center justify-content-center rounded-circle">
              <i class="feather feather-phone-call"></i>
            </span>
            <div>
              <p>Phone</p>
              <span>+1 347-679-8275</span>
            </div>
          </div>
        </li>
        <li>
          <div class="d-flex align-items-center">
            <span class="contact-square d-flex align-items-center justify-content-center rounded-circle">
              <i class="feather feather-message-square"></i>
            </span>
            <div>
              <p class="text-start">Message</p>
              <span>Need this script</span>
            </div>
          </div>
        </li>
        <li>
          <div class="d-flex align-items-center">
            <span class="contact-square d-flex align-items-center justify-content-center rounded-circle">
              <i class="feather feather-calendar"></i>
            </span>
            <div>
              <p class="text-start">Date</p>
              <span>28 Sep 2023</span>
            </div>
          </div>
        </li>
        <li>
          <a href="javascript:;" class="float-xl-end float-lg-start btn btn-primary" data-bs-toggle="modal"
            data-bs-target="#contact_reply">Reply</a>
        </li>
      </ul>
      <!-- /Page Header -->

      <div class="content-page-header">
        <h6>Customers</h6>
        <div class="list-btn">
          <ul class="filter-list">
            <li>
              <a class="btn btn-filters w-auto popup-toggle"><span class="me-2"><img
                    src="@/assets/img/icons/filter-icon.svg" alt="filter" /></span>Filter
              </a>
            </li>
            <li>
              <a class="btn-filters" href="javascript:void(0);"><span><i class="feather feather-grid"></i></span>
              </a>
            </li>
            <li>
              <a class="active btn-filters" href="javascript:void(0);"><span><i class="feather feather-list"></i></span>
              </a>
            </li>
          </ul>
        </div>
      </div>

      <!-- Table -->
      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'Name'">
                      <h2 class="table-avatar d-flex">
                        <router-link to="/contact-details" class="avatar avatar-sm me-2"><img
                            class="avatar-img rounded-circle" :src="require(`@/assets/img/profiles/${record.Image}`)"
                            alt="User Image" /></router-link>
                        <router-link to="/profile">{{ record.Name }}</router-link>
                      </h2>
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
  <contactdetails-model></contactdetails-model>
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
    title: "Number",
    dataIndex: "Number",
    sorter: {
      compare: (a, b) => {
        a = a.Number.toLowerCase();
        b = b.Number.toLowerCase();
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
];
const data = [
  {
    NUM: "1",
    Image: "avatar-14.jpg",
    Name: "John Smith",
    Email: "john@example.com",
    Number: "+1 989-438-3131",
    Message: "Lorem ipsum dolor sit consectetur",
  },
  {
    NUM: "2",
    Image: "avatar-15.jpg",
    Name: "Johnny",
    Email: "johnny@example.com",
    Number: "+1 843-443-3282",
    Message: "Ut enim ad minim veniam, quis",
  },
  {
    NUM: "3",
    Image: "avatar-16.jpg",
    Name: "Robert",
    Email: "robert@example.com",
    Number: "+1 917-409-0861",
    Message: "Duis aute irure dolor in reprehenderit",
  },
  {
    NUM: "4",
    Image: "avatar-17.jpg",
    Name: "Sharonda",
    Email: "sharon@example.com",
    Number: "+1 956-623-2880",
    Message: "Excepteur sint occaecat cupidatat",
  },
  {
    NUM: 5,
    Image: "avatar-18.jpg",
    Name: "Randall",
    Email: "randall@example.com",
    Number: "+1 707-439-1732",
    Message: "Sed ut perspiciatis unde omnis iste",
  },
  {
    NUM: "6",
    Image: "avatar-19.jpg",
    Name: "Pricilla",
    Email: "pricilla@example.com",
    Number: "+1 559-741-9672",
    Message: "Nemo enim ipsam voluptatem quia",
  },
];
export default {
  data() {
    return {
      columns,
      data,
    };
  },
};
</script>
