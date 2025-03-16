<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>FAQ</h5>
          <div class="list-btn">
            <ul class="filter-list">
              <li>
                <a class="btn btn-filters w-auto popup-toggle" data-bs-toggle="tooltip" data-bs-placement="bottom"
                  title="Filter"><span class="me-2"><img src="@/assets/img/icons/filter-icon.svg"
                      alt="filter" /></span>Filter
                </a>
              </li>
              <li>
                <a class="btn btn-primary" href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#add_faq"><i
                    class="fa fa-plus-circle me-2" aria-hidden="true"></i>Add FAQ</a>
              </li>
            </ul>
          </div>
        </div>
      </div>

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
                  <template #bodyCell="{ column }">
                    <template v-if="column.key === 'action'">
                      <div class="d-flex align-items-center">
                        <a class="btn-action-icon me-2" href="javascript:void(0);" data-bs-toggle="modal"
                          data-bs-target="#edit_faq"><i class="feather feather-edit"></i></a>
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
  <faqmodel></faqmodel>
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
    title: "Title",
    dataIndex: "Title",
    sorter: {
      compare: (a, b) => {
        a = a.Title.toLowerCase();
        b = b.Title.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Category",
    dataIndex: "Category",
    sorter: {
      compare: (a, b) => {
        a = a.Category.toLowerCase();
        b = b.Category.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Details",
    dataIndex: "Details",
    sorter: {
      compare: (a, b) => {
        a = a.Details.toLowerCase();
        b = b.Details.toLowerCase();
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
    Title: "Duis aute irure in reprehenderit in voluptate velit?",
    Category: "19 Dec 2023, 06:12 PM",
    Details: "Ut enim ad minima veniam, quis nostrum exercitationem",
  },
  {
    NUM: "2",
    Title: "Duis aute irure in reprehenderit in voluptate velit?",
    Category: "19 Dec 2023, 06:12 PM",
    Details: "At vero eos et accusamus et iusto odio dignissimos",
  },
  {
    NUM: "3",
    Title: "Excepteur occaecat cupidatat non proident?",
    Category: "19 Dec 2023, 06:12 PM",
    Details: "Nam libero tempore, cum soluta nobis est eligendi optio",
  },
  {
    NUM: "4",
    Title: "Sed ut perspiciatis unde omnis iste natus?",
    Category: "19 Dec 2023, 06:12 PM",
    Details: "Sed ut perspiciatis unde omnis iste natus",
  },
  {
    NUM: "5",
    Title: "Nemo enim ipsam voluptatem quia voluptas sit?",
    Category: "12 Dec 2023, 06:12 PM",
    Details: "Et harum quidem rerum facilis est et expedita distinctio",
  },
  {
    NUM: "6",
    Title: "Neque porro quisquam est, qui dolorem ipsum?",
    Category: "19 Dec 2023, 06:12 PM",
    Details: "Temporibus autem quibusdam et officiis debitis aut rerum",
  },
  {
    NUM: "7",
    Title: "Sed ut perspiciatis unde omnis iste natus?",
    Category: "15 Dec 2023, 06:12 PM",
    Details: "Sed ut perspiciatis unde omnis iste natus",
  },
  {
    NUM: "8",
    Title: "Nemo enim ipsam voluptatem quia voluptas sit?",
    Category: "17 Dec 2023, 06:12 PM",
    Details: "Et harum quidem rerum facilis est et expedita distinctio",
  },
  {
    NUM: "9",
    Title: "Neque porro quisquam est, qui dolorem ipsum?",
    Category: "21 Dec 2023, 06:12 PM",
    Details: "Temporibus autem quibusdam et officiis debitis aut rerum",
  },
];
export default {
  data() {
    return {
      title: "FAQ",
      text: "Add FAQ",
      data,
      columns,
    };
  },
};
</script>
