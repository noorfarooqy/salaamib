<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <div class="page-header">
        <div class="content-page-header">
          <h5>Ticket Overview</h5>
          <div class="list-btn">
            <ul class="filter-list">
              <li>
                <a class="btn btn-primary popup-toggle rounded-circle d-inline-flex p-2" href="javascript:void(0);"><i
                    class="feather feather-filter" aria-hidden="true"></i></a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <!-- /Page Header -->

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

      <div class="ticket-details-group">
        <div class="row align-items-center">
          <div class="col-lg-6 col-md-6 col-12">
            <div class="customer-details">
              <div class="d-flex align-items-center">
                <span class="ticket-widget-img rounded-circle d-inline-flex">
                  <img src="@/assets/img/icons/ticket.svg" alt="" />
                </span>
                <div class="ticket-details-cont">
                  <p>TK-105</p>
                  <h6>New Support Ticket</h6>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-6 col-md-6 col-12">
            <div class="ticket-details text-lg-end text-md-end">
              <span class="badge bg-warning-light text-warning-light">Medium</span>
              <span class="badge bg-success-light ms-2">Paid</span>
            </div>
          </div>
        </div>
      </div>
      <div class="ticket-description-group">
        <h6>Description</h6>
        <p>
          Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor
          incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
          nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
        <p class="mb-0">
          Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor
          incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
          nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
      </div>
      <div class="ticket-information">
        <div class="row align-items-center">
          <div class="col-lg-4 col-md-4 col-12">
            <div class="customer-details">
              <div class="d-flex align-items-center">
                <span class="customer-widget-img d-inline-flex">
                  <img class="rounded-circle" src="@/assets/img/profiles/avatar-15.jpg" alt="" />
                </span>
                <div class="customer-details-cont">
                  <h6>Requester</h6>
                  <p>John Smith</p>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-4 col-12">
            <div class="customer-details">
              <div class="d-flex align-items-center">
                <span class="customer-widget-icon rounded-circle d-inline-flex">
                  <i class="feather feather-calendar"></i>
                </span>
                <div class="customer-details-cont">
                  <h6>Requested Date</h6>
                  <p>30 Dec, 2023</p>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-4 col-12">
            <div class="customer-details border-0">
              <div class="d-flex align-items-center">
                <span class="customer-widget-icon rounded-circle d-inline-flex">
                  <i class="feather feather-file-text"></i>
                </span>
                <div class="customer-details-cont">
                  <h6>Subject</h6>
                  <p>Support Ticket</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="ticket-history ticket-information pb-0">
        <div class="row">
          <div class="col-lg-6 col-md-12">
            <div class="card-inform">
              <div class="ticket-info d-flex align-items-center justify-content-between">
                <h6>Attachments</h6>
                <label class="ticket-upload upload-doc mb-0">
                  <span class="report-info"><i class="feather feather-paperclip me-2"></i></span>Add File
                  <input type="file" multiple="" id="image_personal" />
                </label>
              </div>
            </div>
            <!-- Support Ticket -->
            <div class="support-details d-flex align-items-center justify-content-between">
              <div class="d-flex align-items-center">
                <span class="support-widget-icon rounded-circle d-inline-flex">
                  <i class="feather feather-file-text"></i>
                </span>
                <div class="support-details-cont">
                  <h6>New Support Ticket</h6>
                  <p>3.7MB</p>
                </div>
              </div>
              <div class="d-flex align-items-center">
                <a class="btn-action-icon me-2" href="javascript:void(0);" download><i
                    class="feather feather-download"></i></a>
                <div class="dropdown dropdown-action">
                  <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown" aria-expanded="false"><i
                      class="fas fa-ellipsis-v"></i></a>
                  <div class="dropdown-menu dropdown-menu-right">
                    <ul>
                      <li>
                        <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-edit me-2"></i>Edit</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="javascript:void(0);"><i
                            class="far fa-trash-alt me-2"></i>Delete</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <!-- /Support Ticket -->

            <!-- Support Ticket -->
            <div class="support-details d-flex align-items-center justify-content-between">
              <div class="d-flex align-items-center">
                <span class="support-widget-icon rounded-circle d-inline-flex">
                  <i class="feather feather-file-text"></i>
                </span>
                <div class="support-details-cont">
                  <h6>New Support Ticket</h6>
                  <p>3.7MB</p>
                </div>
              </div>
              <div class="d-flex align-items-center">
                <a class="btn-action-icon me-2" href="javascript:void(0);" download><i
                    class="feather feather-download"></i></a>
                <div class="dropdown dropdown-action">
                  <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown" aria-expanded="false"><i
                      class="fas fa-ellipsis-v"></i></a>
                  <div class="dropdown-menu dropdown-menu-right">
                    <ul>
                      <li>
                        <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-edit me-2"></i>Edit</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="javascript:void(0);"><i
                            class="far fa-trash-alt me-2"></i>Delete</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <!-- /Support Ticket -->

            <!-- Support Ticket -->
            <div class="support-details d-flex align-items-center justify-content-between">
              <div class="d-flex align-items-center">
                <span class="support-widget-icon rounded-circle d-inline-flex">
                  <i class="feather feather-file-text"></i>
                </span>
                <div class="support-details-cont">
                  <h6>New Support Ticket</h6>
                  <p>3.7MB</p>
                </div>
              </div>
              <div class="d-flex align-items-center">
                <a class="btn-action-icon me-2" href="javascript:void(0);" download><i
                    class="feather feather-download"></i></a>
                <div class="dropdown dropdown-action">
                  <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown" aria-expanded="false"><i
                      class="fas fa-ellipsis-v"></i></a>
                  <div class="dropdown-menu dropdown-menu-right">
                    <ul>
                      <li>
                        <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-edit me-2"></i>Edit</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="javascript:void(0);"><i
                            class="far fa-trash-alt me-2"></i>Delete</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <!-- /Support Ticket -->

            <!-- Support Ticket -->
            <div class="support-details d-flex align-items-center justify-content-between">
              <div class="d-flex align-items-center">
                <span class="support-widget-icon rounded-circle d-inline-flex">
                  <i class="feather feather-file-text"></i>
                </span>
                <div class="support-details-cont">
                  <h6>New Support Ticket</h6>
                  <p>3.7MB</p>
                </div>
              </div>
              <div class="d-flex align-items-center">
                <a class="btn-action-icon me-2" href="javascript:void(0);" download><i
                    class="feather feather-download"></i></a>
                <div class="dropdown dropdown-action">
                  <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown" aria-expanded="false"><i
                      class="fas fa-ellipsis-v"></i></a>
                  <div class="dropdown-menu dropdown-menu-right">
                    <ul>
                      <li>
                        <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-edit me-2"></i>Edit</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="javascript:void(0);"><i
                            class="far fa-trash-alt me-2"></i>Delete</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <!-- /Support Ticket -->
          </div>
          <div class="col-lg-6 col-md-12">
            <div class="card-inform">
              <div class="ticket-info d-flex align-items-center justify-content-between">
                <h6>History</h6>
              </div>
            </div>
            <div class="card-inform d-block mt-lg-5 mt-0">
              <ul class="activity-feed">
                <li class="feed-item">
                  <span class="feed-text"><strong class="text-gray-dark me-2">John Smith</strong> Created a
                    new response Created a new response</span>
                  <p>30 Dec 2023 01:24AM</p>
                </li>
                <li class="feed-item">
                  <span class="feed-text"><strong class="text-gray-dark me-2">Forest Kroch </strong> Lorem
                    ipsum dolor sit amet,</span>
                  <p>24 Dec 2023 10:36AM</p>
                </li>
                <li class="feed-item">
                  <span class="feed-text"><strong class="text-gray-dark me-2">Townsend Seary </strong> Sed ut
                    perspiciatis unde</span>
                  <p>18 Dec 2023 09:18PM</p>
                </li>
                <li class="feed-item">
                  <span class="feed-text"><strong class="text-gray-dark me-2">Margaretta Worvell </strong>
                    Nemo enim ipsam voluptatem</span>
                  <p>19 Jan 2023 09:18PM</p>
                </li>
                <li class="feed-item">
                  <span class="feed-text"><strong class="text-gray-dark me-2">Harald Kowalski </strong> Neque
                    porro quisquam est, qui dolorem</span>
                  <p>12 May 2023 09:18PM</p>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <!-- comments -->
      <div class="comments">
        <div class="comments-head">
          <h5>Comments</h5>
        </div>
        <!-- card -->
        <div class="card" v-for="item in ticketcommand" :key="item.id">
          <div class="card-body">
            <div class="comments-details d-flex align-items-center justify-content-between">
              <div class="d-flex align-items-center">
                <span class="comments-widget-img rounded-circle d-inline-flex">
                  <img class="avatar-img rounded-circle" :src="require(`@/assets/img/profiles/${item.img}`)"
                    alt="User Image" />
                </span>
                <div class="comments-details-cont">
                  <h6>{{ item.name }}</h6>
                  <p>a week ago</p>
                </div>
              </div>
              <a href="javascript:;" class="reply-comment d-flex"><span><i
                    class="feather feather-corner-down-left me-2"></i></span>Reply</a>
            </div>
            <div class="card-describe">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed eiusmod
                tempor incididunt labore dolore magna aliqua. Ut enim minim veniam,
                nostrud exercitation ullamco laboris nisi ut aliquip ex commodo
                consequat. Duis aute non proident, sunt in culpa qui officia deserunt
                mollit anim id est laborum.
              </p>
            </div>
          </div>
        </div>
        <!-- /card -->
      </div>
      <!-- /comments -->

      <div class="comments">
        <div class="row">
          <div class="col-lg-12">
            <div class="input-block mb-3">
              <label>Leave a comments</label>
              <input type="text" class="form-control" placeholder="Enter Comments">
            </div>
          </div>
          <div class="col-lg-12">
            <div class="text-end">
              <button type="submit" class="btn btn-primary">Post Comments</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->

  <!-- Add Asset -->
  <div class="toggle-sidebar">
    <div class="sidebar-layout-filter">
      <div class="sidebar-header">
        <h5>Filter</h5>
        <div class="d-flex">
          <div class="dropdown dropdown-action">
            <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown" aria-expanded="false"><i
                class="fas fa-ellipsis-v"></i></a>
            <div class="dropdown-menu dropdown-menu-end">
              <ul>
                <li>
                  <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-edit me-2"></i>Edit</a>
                </li>
                <li>
                  <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-trash-alt me-2"></i>Delete</a>
                </li>
                <li>
                  <a class="dropdown-item" href="javascript:void(0);"><i class="far fa-eye me-2"></i>View</a>
                </li>
              </ul>
            </div>
          </div>
          <a href="javascript:;" class="sidebar-closes ms-3"><i class="fa-regular fa-circle-xmark"></i></a>
        </div>
      </div>
      <div class="sidebar-body">
        <b-form action="javascript:;" autocomplete="off">
          <div class="form-group-item ticket-sidebar">
            <div class="row">
              <div class="col-lg-12">
                <div class="form-group">
                  <label>Ticket Status</label>
                  <div class="task-priority-btn select-status justify-content-center table-project-subtitle">
                    <select onchange="this.className=this.options[this.selectedIndex].className" class="selecttext">
                      <option class="selecttext" value="select">Status</option>
                      <option class="greentext" value="apple">Done</option>
                      <option class="bluetext" value="inprogress">In Progress</option>
                      <option class="orangetext" value="pending">Waiting</option>
                    </select>
                  </div>
                </div>
              </div>
              <div class="col-lg-12">
                <div class="form-group">
                  <label>Ticket Type</label>
                  <vue-select :options="Ticket" id="ticket" placeholder="Select Ticket" />
                </div>
              </div>
              <div class="col-lg-12">
                <div class="form-group">
                  <label>Assigned To</label>
                  <vue-select :options="Assigned" id="assignedto" placeholder="Select Assigned" />
                </div>
              </div>
              <div class="col-lg-12">
                <div class="form-group">
                  <label>Project</label>
                  <a class="action-sets" href="javascript:;" data-bs-toggle="dropdown" aria-expanded="false">
                    <span><i class="fa-solid fa-circle text-warning-light me-1"></i>
                      Medium</span>
                    <img src="@/assets/img/icons/arrow-down.svg" width="15" alt="img" />
                  </a>
                  <ul class="dropdown-menu action-drop">
                    <li>
                      <a href="javascript:;" class="dropdown-item"><i
                          class="fa-solid fa-circle info-border me-2 text-info"></i>
                        High</a>
                    </li>
                    <li>
                      <a href="javascript:;" class="dropdown-item"><i
                          class="fa-solid fa-circle warning-border me-2 text-warning-light"></i>
                        Medium</a>
                    </li>
                    <li>
                      <a href="javascript:;" class="dropdown-item"><i
                          class="fa-solid fa-circle danger-border me-2 text-danger-light"></i>
                        Low</a>
                    </li>
                  </ul>
                </div>
              </div>
              <div class="col-lg-12">
                <div class="form-group">
                  <label>Project</label>
                  <vue-select :options="Project" id="project" placeholder="Select Project" />
                </div>
              </div>
              <div class="col-lg-12">
                <div class="form-group">
                  <label class="form-control-label">Due Date</label>
                  <div class="cal-icon">
                    <date-picker v-model="startdate" class="datetimepicker form-control" :editable="true"
                      :clearable="false" :input-format="dateFormat" />
                  </div>
                </div>
              </div>
              <div class="col-lg-12">
                <div class="form-group">
                  <label>Category</label>
                  <vue-select :options="Category" id="category" placeholder="Select Category" />
                </div>
              </div>
            </div>
          </div>
        </b-form>
      </div>
    </div>
  </div>
  <!-- /Add Assets -->
</template>
<script>
import { ref } from "vue";
const currentDate = ref(new Date());
import ticketcommand from "@/assets/json/ticketcommand.json";
export default {
  setup() {
    return {
      startdate: currentDate,
      dateFormat: "dd-MM-yyyy",
      ticketcommand: ticketcommand,
      Ticket: ["Select Ticket", "Task 1", "Task 2", "Task 3"],
      Project: ["Select Project", "Project 1", "Project 2", "Project 3"],
      Category: ["Select Category", "Category 1", "Category 2", "Category 3"],
      Assigned: ["Select Assigned", "John Smith", "Johnson", "Randall"],
    };
  },
  mounted() {
    var popupToggleElements = document.getElementsByClassName("popup-toggle");
    if (popupToggleElements.length > 0) {
      for (var i = 0; i < popupToggleElements.length; i++) {
        popupToggleElements[i].addEventListener("click", function () {
          var toggleSidebar = document.getElementsByClassName("toggle-sidebar")[0];
          if (toggleSidebar) {
            toggleSidebar.classList.add("open-filter");
          }
        });
      }

      var sidebarClosesElements = document.getElementsByClassName("sidebar-closes");
      for (var j = 0; j < sidebarClosesElements.length; j++) {
        sidebarClosesElements[j].addEventListener("click", function () {
          var toggleSidebar = document.getElementsByClassName("toggle-sidebar")[0];
          if (toggleSidebar) {
            toggleSidebar.classList.remove("open-filter");
          }
        });
      }
    }
  },
};
</script>
