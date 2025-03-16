<template>
  <!-- Page Header -->
  <div class="page-header">
    <div class="content-page-header">
      <h5>Customer Ledger</h5>
      <div class="list-btn">
        <ul class="filter-list">
          <li>
            <a
              class="btn btn-filters w-auto popup-toggle"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="Filter"
              ><span class="me-2"
                ><img src="@/assets/img/icons/filter-icon.svg" alt="filter" /></span
              >Filter
            </a>
          </li>
          <li>
            <a
              class="active btn-filters"
              href="javascript:void(0);"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="List-View"
              ><span><i class="feather feather-list"></i></span>
            </a>
          </li>
          <li>
            <a
              class="btn-filters"
              href="javascript:void(0);"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="Grid-View"
              ><span><i class="feather feather-grid"></i></span>
            </a>
          </li>
          <li>
            <div
              class="dropdown dropdown-action"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="Download"
            >
              <a
                href="javascript:;"
                class="btn-filters"
                data-bs-toggle="dropdown"
                aria-expanded="false"
                ><span><i class="feather feather-download"></i></span
              ></a>
              <div class="dropdown-menu dropdown-menu-end">
                <ul class="d-block">
                  <li>
                    <a
                      class="d-flex align-items-center download-item"
                      href="javascript:void(0);"
                      download
                      ><i class="far fa-file-pdf me-2"></i>PDF</a
                    >
                  </li>
                  <li>
                    <a
                      class="d-flex align-items-center download-item"
                      href="javascript:void(0);"
                      download
                      ><i class="far fa-file-text me-2"></i>CVS</a
                    >
                  </li>
                </ul>
              </div>
            </div>
          </li>
          <li>
            <a
              class="btn-filters"
              href="javascript:void(0);"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="Print"
              ><span><i class="feather feather-printer"></i></span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <!-- /Page Header -->
</template>
